"""Motor de assessment de madurez FinOps (determinista, sin LLM, solo biblioteca estandar).

Subcomandos:
  init   --scope NOMBRE --out cuestionario.json [--caps slug1,slug2]
         Genera el cuestionario con todos los criterios Crawl/Walk/Run de la base de conocimiento.
  score  cuestionario.json [--out informe.md] [--json resultado.json]
         Calcula madurez por capacidad y dominio, brechas y plan de mejora.
  plan   resultado.json [--top N]
         Lista las acciones concretas (criterios no cumplidos del siguiente nivel) priorizadas.

Estados de cada criterio: cumple | parcial | no | na | superado | sin_datos
  (cumple = la afirmacion describe a la organizacion hoy; superado = describia un nivel que ya se dejo atras)
Puntaje por criterio: cumple=1, parcial=0.5, no=0, sin_datos=0 (marcado como no evaluado), na se excluye.

Regla de nivel (HEURISTICA PROPIA, no es el puntaje oficial de la FinOps Foundation):
  Un nivel se considera alcanzado si cumple >= UMBRAL (0.75) de sus criterios aplicables;
  el nivel de la capacidad es el mas alto alcanzado y los inferiores se dan por superados.
  Puntaje continuo 0-3 = niveles alcanzados + fraccion del siguiente nivel.
  0 = Pre-Crawl, 1 = Crawl, 2 = Walk, 3 = Run.

Base de conocimiento: <FINOPS_HOME>/kb/capabilities.json (finops.org, CC BY 4.0, FinOps Foundation).
"""
import argparse
import json
import sys
from pathlib import Path

KB = Path(__file__).resolve().parent.parent / "kb" / "capabilities.json"
UMBRAL = 0.75
NIVELES = ["crawl", "walk", "run"]
LENTES = ["knowledge", "process", "metrics", "adoption", "automation"]  # FinOps Assessment Guide, escala 0-4
META_PCT = 60.0  # Target Score por defecto: 12 de 20 (ejemplo de la guia oficial)
MIN_COBERTURA_PCT = 50.0  # HEURISTICA: bajo este % de criterios con evidencia no se declara nivel
NOMBRE_NIVEL = {0: "Pre-Crawl", 1: "Crawl", 2: "Walk", 3: "Run"}
PUNTOS = {"cumple": 1.0, "parcial": 0.5, "no": 0.0, "sin_datos": 0.0}
DOMINIOS_ES = {
    "Understand Usage & Cost": "Comprender el uso y el costo",
    "Quantify Business Value": "Cuantificar el valor de negocio",
    "Optimize Usage & Cost": "Optimizar el uso y el costo",
    "Manage the FinOps Practice": "Gestionar la práctica FinOps",
}


def cargar_kb():
    if not KB.exists():
        sys.exit("Falta kb/capabilities.json. El texto del framework no se distribuye: genérelo con "
                 "scripts/scrape_raw.py y scripts/build_kb.py (requiere Playwright).")
    return json.loads(KB.read_text(encoding="utf-8"))


def cmd_init(a):
    kb = cargar_kb()
    sel = set(a.caps.split(",")) if a.caps else None
    doc = {"organizacion": a.scope, "fecha": "", "alcance_finops": a.scope,
           "nota": "Estados: cumple | parcial | no | na | sin_datos. Complete evidencia por criterio.",
           "capacidades": {}}
    for c in kb:
        if sel and c["slug"] not in sel:
            continue
        doc["capacidades"][c["slug"]] = {
            "nombre": c["name"], "dominio": c["domain"],
            "prioridad_negocio": 2,  # 1 baja, 2 media, 3 alta
            # Modo oficial FinOps Assessment Guide: 5 lentes, 0-4 (null = sin evaluar)
            "lentes": {l: None for l in LENTES},
            "peso_lentes": {l: 1.0 for l in LENTES},
            "meta_pct": META_PCT,
            "criterios": {n: [{"texto": t, "estado": "sin_datos", "evidencia": ""}
                              for t in c["maturity"][n.capitalize()]] for n in NIVELES},
        }
    Path(a.out).write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Cuestionario: {a.out} ({len(doc['capacidades'])} capacidades)")


def evaluar_capacidad(cap):
    """Los criterios describen el estado de cada nivel (no son requisitos acumulativos).
    Nivel alcanzado = el mas alto cuyos criterios aplicables se cumplen >= UMBRAL; los niveles
    inferiores se dan por superados. Estados 'na' y 'superado' se excluyen del calculo."""
    res, fracs = {}, {}
    for n in NIVELES:
        crit = [x for x in cap["criterios"][n] if x["estado"] not in ("na", "superado")]
        eval_ = [x for x in crit if x["estado"] != "sin_datos"]
        pts = sum(PUNTOS[x["estado"]] for x in crit)
        frac = pts / len(crit) if crit else 0.0
        fracs[n] = frac
        res[n] = {"fraccion": round(frac, 3), "criterios": len(crit), "evaluados": len(eval_),
                  "alcanzado": bool(crit) and frac >= UMBRAL}
    alcanzado = 0
    for i, n in enumerate(NIVELES, start=1):
        if res[n]["alcanzado"]:
            alcanzado = i
    for i, n in enumerate(NIVELES, start=1):
        if i < alcanzado:
            res[n]["alcanzado"] = True  # nivel inferior implicito
    if alcanzado == 3:
        puntaje = 3.0
    else:
        puntaje = alcanzado + fracs[NIVELES[alcanzado]]
    return res, alcanzado, round(puntaje, 2)


def evaluar_lentes(cap):
    """Puntaje oficial: % del maximo ponderado (lentes 0-4). None si no hay lentes evaluados."""
    pts, mx, det = 0.0, 0.0, {}
    for l in LENTES:
        v = (cap.get("lentes") or {}).get(l)
        w = (cap.get("peso_lentes") or {}).get(l, 1.0)
        det[l] = v
        if v is None or w <= 0:
            continue
        pts += v * w
        mx += 4 * w
    if mx == 0:
        return None
    pct = round(100 * pts / mx, 1)
    meta = cap.get("meta_pct", META_PCT)
    debiles = sorted([(v, l) for l, v in det.items() if v is not None])[:2]
    return {"pct": pct, "meta_pct": meta, "brecha_pct": round(max(0.0, meta - pct), 1),
            "lentes": det, "lentes_mas_debiles": [l for _, l in debiles],
            "lentes_sin_evaluar": [l for l, v in det.items() if v is None]}


def acciones(cap, nivel_actual):
    """Criterios no cumplidos del siguiente nivel (o del actual si queda incompleto)."""
    objetivo = NIVELES[min(nivel_actual, 2)] if nivel_actual < 3 else None
    if not objetivo:
        return objetivo, []
    pend = [x for x in cap["criterios"][objetivo] if x["estado"] in ("no", "parcial", "sin_datos")]
    pend.sort(key=lambda x: {"parcial": 0, "no": 1, "sin_datos": 2}[x["estado"]])
    return objetivo, pend


def cmd_score(a):
    doc = json.loads(Path(a.file).read_text(encoding="utf-8"))
    out = {"organizacion": doc.get("organizacion"), "capacidades": {}, "dominios": {}}
    for slug, cap in doc["capacidades"].items():
        niv, alc, pje = evaluar_capacidad(cap)
        obj, pend = acciones(cap, alc)
        sin = sum(v["criterios"] - v["evaluados"] for v in niv.values())
        total = sum(v["criterios"] for v in niv.values())
        cobertura = round(100 * (total - sin) / total, 1) if total else 0.0
        concluyente = cobertura >= MIN_COBERTURA_PCT
        lens = evaluar_lentes(cap)
        out["capacidades"][slug] = {
            "lentes": lens,
            "nombre": cap["nombre"], "dominio": cap["dominio"], "nivel": alc,
            "nivel_nombre": NOMBRE_NIVEL[alc] if concluyente else "No concluyente",
            "concluyente": concluyente, "cobertura_pct": cobertura, "puntaje": pje, "detalle": niv,
            "prioridad_negocio": cap.get("prioridad_negocio", 2),
            "sin_evaluar": sin, "nivel_objetivo": obj,
            "acciones": [{"texto": x["texto"], "estado": x["estado"], "evidencia": x.get("evidencia", "")}
                         for x in pend],
        }
    por_dom = {}
    for s, c in out["capacidades"].items():
        if c["concluyente"]:
            por_dom.setdefault(c["dominio"], []).append(c["puntaje"])
    for d, v in por_dom.items():
        out["dominios"][d] = round(sum(v) / len(v), 2)
    tot = [c["puntaje"] for c in out["capacidades"].values() if c["concluyente"]]
    out["global"] = round(sum(tot) / len(tot), 2) if tot else None
    if a.json:
        Path(a.json).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    informe = render(out)
    if a.out:
        Path(a.out).write_text(informe, encoding="utf-8")
        print(f"Informe: {a.out}")
    else:
        print(informe)


def barra(p):
    llenos = int(round(p / 3 * 12))
    return "[" + "#" * llenos + "." * (12 - llenos) + "]"


def prioridad(c):
    # brecha al siguiente nivel ponderada por prioridad de negocio; menor esfuerzo primero
    brecha = (c["nivel"] + 1) - c["puntaje"] if c["nivel"] < 3 else 0
    return round(brecha * c["prioridad_negocio"], 2)


def render(o):
    L = [f"# Informe de madurez FinOps - {o['organizacion']}", "",
         "Método: criterios Crawl/Walk/Run del FinOps Framework (FinOps Foundation, CC BY 4.0). "
         f"El puntaje 0-3 y el umbral de {int(UMBRAL*100)} % son una heurística de este proyecto, "
         "no el puntaje oficial del FinOps Assessment.", "",
         ("Madurez global: no concluyente (ninguna capacidad alcanza la cobertura mínima de evidencia)" if o["global"] is None else f"Madurez global: {o['global']} / 3 (solo capacidades con evidencia suficiente)"), "", "## Por dominio", "",
         "| Dominio | Puntaje | Gráfico |", "|---|---|---|"]
    for d, p in o["dominios"].items():
        L.append(f"| {DOMINIOS_ES.get(d, d)} | {p} | {barra(p)} |")
    L += ["", "## Por capacidad", "", "| Capacidad | Nivel | Puntaje | Evaluado | Sin evaluar | Prioridad negocio |", "|---|---|---|---|---|---|"]
    for s, c in sorted(o["capacidades"].items(), key=lambda kv: (kv[1]["dominio"], kv[0])):
        pj = f"{c['puntaje']} {barra(c['puntaje'])}" if c["concluyente"] else "-"
        L.append(f"| {c['nombre']} | {c['nivel_nombre']} | {pj} | {c['cobertura_pct']} % | {c['sin_evaluar']} | {c['prioridad_negocio']} |")
    L += ["", "## Brechas priorizadas (brecha x prioridad de negocio)", ""]
    rank = sorted(o["capacidades"].values(), key=prioridad, reverse=True)
    for i, c in enumerate([r for r in rank if r["nivel"] < 3 and r["concluyente"]][:8], 1):
        L.append(f"{i}. {c['nombre']}: {c['nivel_nombre']} -> {NOMBRE_NIVEL[c['nivel']+1]} (índice {prioridad(c)})")
        for x in c["acciones"][:4]:
            L.append(f"   - [{x['estado']}] {x['texto']}")
    con_lentes = {k: c for k, c in o["capacidades"].items() if c.get("lentes")}
    if con_lentes:
        L += ["", "## Modo oficial: 5 lentes (FinOps Assessment Guide, escala 0-4)", "",
              "| Capacidad | K | P | M | A | Au | % | Meta % | Brecha |", "|---|---|---|---|---|---|---|---|---|"]
        for c in sorted(con_lentes.values(), key=lambda c: -c["lentes"]["brecha_pct"]):
            ln = c["lentes"]["lentes"]
            f = lambda v: "-" if v is None else str(v)
            L.append(f"| {c['nombre']} | {f(ln['knowledge'])} | {f(ln['process'])} | {f(ln['metrics'])} | "
                     f"{f(ln['adoption'])} | {f(ln['automation'])} | {c['lentes']['pct']} | "
                     f"{c['lentes']['meta_pct']} | {c['lentes']['brecha_pct']} |")
        L += ["", "K=Knowledge, P=Process, M=Metrics, A=Adoption, Au=Automation. Los lentes más débiles de cada "
                  "capacidad con brecha son el foco de la hoja de ruta (Stage 4: Focus)."]
    nc = [c["nombre"] for c in o["capacidades"].values() if not c["concluyente"]]
    if nc:
        L += ["", f"No concluyente (menos de {int(MIN_COBERTURA_PCT)} % de criterios con evidencia): {', '.join(nc)}. "
                  "Falta entrevista o evidencia; no se calcula nivel ni brecha para ellas."]
    sd = sum(c["sin_evaluar"] for c in o["capacidades"].values())
    if sd:
        L += ["", f"Advertencia: {sd} criterios quedaron sin_datos y puntúan 0; el resultado es conservador.", ]
    return "\n".join(L)


def cmd_plan(a):
    o = json.loads(Path(a.file).read_text(encoding="utf-8"))
    rank = sorted([c for c in o["capacidades"].values() if c["nivel"] < 3 and c["concluyente"]], key=prioridad, reverse=True)
    for c in rank[:a.top]:
        print(f"\n== {c['nombre']} ({c['nivel_nombre']} -> {NOMBRE_NIVEL[c['nivel']+1]}) indice {prioridad(c)}")
        for x in c["acciones"]:
            print(f"  [{x['estado']}] {x['texto']}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    i = sp.add_parser("init"); i.add_argument("--scope", required=True); i.add_argument("--out", required=True)
    i.add_argument("--caps"); i.set_defaults(f=cmd_init)
    s = sp.add_parser("score"); s.add_argument("file"); s.add_argument("--out"); s.add_argument("--json")
    s.set_defaults(f=cmd_score)
    q = sp.add_parser("plan"); q.add_argument("file"); q.add_argument("--top", type=int, default=5)
    q.set_defaults(f=cmd_plan)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
