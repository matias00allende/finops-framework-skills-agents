"""Propone estados de criterios Crawl/Walk/Run a partir de evidencia medida por los recolectores
(aws_evidencia.py; los formatos de GCP y Azure quedan previstos para la v2).

Uso: python -I mapear_evidencia.py cuestionario.json evidencia.json [--out cuestionario_pre.json]

Detecta la nube por las claves del JSON, normaliza los datos a un formato comun y aplica reglas.
Solo completa criterios con estado `sin_datos`. Cada propuesta lleva `origen: "evidencia_automatica"`,
`nube`, la evidencia numerica y una `confianza` (alta | media | baja). La persona que conduce el
assessment debe confirmar o corregir cada propuesta: la API mide configuracion y cobertura, no si el
equipo entiende o sigue el proceso.

Los umbrales marcados HEURISTICA son de este proyecto; el FinOps Framework no publica umbrales
numericos por nivel en el texto de las capacidades.
Cobertura de reglas: AWS (12 criterios), GCP y Azure solo allocation, budgeting y data ingestion
(sus recolectores NO estan probados contra cuentas reales, por lo que las propuestas heredan esa reserva).
"""
import argparse
import json
from pathlib import Path


def detectar_nube(ev):
    if "cuenta_facturacion" in ev:
        return "gcp"
    if "scope" in ev:
        return "azure"
    return "aws"


def normalizar(ev):
    """Devuelve un dict comun: tag_min, sp_cob, anomalias, presupuestos, ingestion."""
    nube = detectar_nube(ev)
    n = {"nube": nube, "tag_min": None, "sp_cob": None, "anomalias": None, "presupuestos": None, "ingestion": None}

    def minimo(meses):
        vals = [m["pct_asignado"] for m in (meses or []) if isinstance(m, dict) and m.get("pct_asignado") is not None]
        return min(vals) if vals else None

    if nube == "aws":
        n["tag_min"] = minimo((ev.get("allocation_tag_coverage") or {}).get("meses"))
        s = (ev.get("rate_optimization") or {}).get("savings_plans_cobertura_pct") or []
        n["sp_cob"] = s[-1]["pct"] if s else None
        n["anomalias"] = ev.get("anomaly_management")
        b = ev.get("budgeting")
        if b is not None:
            n["presupuestos"] = {"total": len(b), "notificaciones": sum((x.get("notificaciones") or 0) for x in b),
                                 "acciones": sum((x.get("acciones") or 0) for x in b),
                                 "integraciones": 0,
                                 "tipos": [x.get("tipo") or "" for x in b]}
        d = ev.get("data_ingestion")
        if d is not None:
            foc = [e for e in d.get("data_exports", []) if "FOCUS" in (e.get("tabla") or "").upper()]
            n["ingestion"] = {"total": len(d.get("cur_legado") or []) + len(d.get("data_exports") or []),
                              "focus": len(foc)}
    elif nube == "gcp":
        n["tag_min"] = minimo((ev.get("allocation") or {}).get("meses"))
        b = ev.get("budgeting")
        if isinstance(b, dict):
            n["presupuestos"] = {"total": b.get("total", 0), "notificaciones": b.get("total", 0),
                                 "acciones": 0, "integraciones": b.get("con_pubsub", 0), "tipos": []}
        d = ev.get("data_ingestion")
        if isinstance(d, dict):
            exp = d.get("exports") or {}
            n["ingestion"] = {"total": sum(len(v) for v in exp.values() if isinstance(v, list)),
                              "focus": len(exp.get("focus") or [])}
    else:  # azure
        n["tag_min"] = minimo((ev.get("allocation_tag_coverage") or {}).get("meses"))
        b = ev.get("budgeting")
        if isinstance(b, dict):
            ps = b.get("presupuestos") or []
            notif = [x for p in ps for x in p.get("notificaciones", [])]
            n["presupuestos"] = {"total": b.get("total", len(ps)), "notificaciones": len(notif), "acciones": 0,
                                 "integraciones": sum(1 for x in notif if x.get("action_groups")), "tipos": []}
        d = ev.get("data_ingestion")
        if isinstance(d, dict):
            n["ingestion"] = {"total": d.get("total", 0), "focus": d.get("focus", 0)}
    return n


# ----------------------------------------------------------------------------- reglas

def r_alloc_mayoria(n):
    v = n["tag_min"]
    if v is None:
        return None
    return ("cumple" if v > 50 else "no", f"Gasto asignado por tag/label, minimo mensual {v} %", "alta")


def r_alloc_alta(n):  # HEURISTICA: >=90 cumple, >=70 parcial
    v = n["tag_min"]
    if v is None:
        return None
    est = "cumple" if v >= 90 else "parcial" if v >= 70 else "no"
    return (est, f"Gasto asignado por tag/label, minimo mensual {v} % (umbral heuristico 90 %/70 %)", "media")


def r_anom_deteccion(n):
    a = n["anomalias"]
    if a is None:
        return None
    k = len(a["monitores"])
    return ("cumple" if k else "no", f"{k} monitor(es) de Cost Anomaly Detection", "alta")


def r_anom_umbral(n):
    a = n["anomalias"]
    if not a:
        return None
    con = [s for s in a["suscripciones"] if s.get("umbral")]
    return ("cumple" if con else "no", f"{len(con)} suscripcion(es) con umbral configurado", "alta")


def r_anom_ruteo(n):
    a = n["anomalias"]
    if not a:
        return None
    subs = a["suscripciones"]
    if not subs:
        return ("no", "Sin suscripciones de alerta", "alta")
    tipos = {t for s in subs for t in s.get("suscriptores", [])}
    return ("parcial", f"{len(subs)} suscripcion(es), tipos de suscriptor {sorted(tipos)}; "
            "no se verifica ruteo por equipo propietario", "media")


def r_anom_ticketing(n):
    a = n["anomalias"]
    if not a:
        return None
    tipos = {t for s in a["suscripciones"] for t in s.get("suscriptores", [])}
    return ("parcial" if "SNS" in tipos else "no",
            f"Tipos de suscriptor: {sorted(tipos)} (SNS permite integrar con ticketing)", "media")


def r_anom_budget_vs_servicio(n):  # describe Crawl: usa alertas de presupuesto en vez de deteccion
    a = n["anomalias"]
    if a is None:
        return None
    return ("no" if a["monitores"] else "cumple", f"{len(a['monitores'])} monitor(es) de anomalias existentes", "alta")


def r_budget_acciones(n):
    b = n["presupuestos"]
    if b is None:
        return None
    if b["acciones"]:
        est = "cumple"
    elif b["integraciones"]:
        est = "parcial"  # hay integracion programatica (Pub/Sub, action group) pero no se prueba una accion de control
    else:
        est = "parcial" if b["notificaciones"] else "no"
    return (est, f"{b['total']} presupuesto(s), {b['notificaciones']} notificacion(es), "
            f"{b['acciones']} accion(es) automatica(s), {b['integraciones']} integracion(es) programatica(s)", "media")


def r_rate_alerta_util(n):
    b = n["presupuestos"]
    if b is None or n["nube"] != "aws":
        return None
    hay = [t for t in b["tipos"] if "SAVINGS_PLANS" in t or "RI_" in t]
    return ("cumple" if hay else "no",
            f"Presupuestos de utilizacion de compromisos: {len(hay) or 'ninguno detectado (puede existir otra alerta)'}",
            "media" if hay else "baja")


def r_rate_cobertura_baja(n):  # describe Crawl; HEURISTICA: >=60 % no describe la organizacion
    v = n["sp_cob"]
    if v is None:
        return None
    return ("no" if v >= 60 else "cumple", f"Cobertura de Savings Plans ultimo mes {v} % (umbral heuristico 60 %)", "media")


def r_ing_resumen(n):
    d = n["ingestion"]
    if d is None:
        return None
    return ("cumple" if d["total"] else "no", f"{d['total']} export(s)/informe(s) de costo y uso configurados", "alta")


def r_ing_focus(n):
    d = n["ingestion"]
    if d is None:
        return None
    return ("cumple" if d["focus"] else "no",
            f"Exports tipo FOCUS: {d['focus']} (de {d['total']}); el criterio admite tambien herramientas de terceros",
            "alta" if d["focus"] else "baja")


# (slug, prefijo del texto del criterio, regla)
REGLAS = [
    ("allocation", "A majority of total costs can often be allocated directly", r_alloc_mayoria),
    ("allocation", "Advanced practices reach consistently high levels of allocation coverage", r_alloc_alta),
    ("anomaly-management", "Some form of automated detection", r_anom_deteccion),
    ("anomaly-management", "Context-relevant thresholds are detected", r_anom_umbral),
    ("anomaly-management", "Unexpected spending automatically routed", r_anom_ruteo),
    ("anomaly-management", "Anomaly alerts of an appropriate scale or urgency can integrate", r_anom_ticketing),
    ("anomaly-management", "Using budget alerts vs an anomaly detection service", r_anom_budget_vs_servicio),
    ("budgeting", "Live execution thresholds are enforced", r_budget_acciones),
    ("rate-optimization", "Alerting put in place when commitment utilization declines", r_rate_alerta_util),
    ("rate-optimization", "Coverage rates or effective discounts are likely very low", r_rate_cobertura_baja),
    ("data-ingestion", "Use of summarized cost and usage data file", r_ing_resumen),
    ("data-ingestion", "Use of one or more third party FinOps tools or platforms to normalize data, or use of FOCUS", r_ing_focus),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cuestionario")
    ap.add_argument("evidencia")
    ap.add_argument("--out")
    a = ap.parse_args()
    q = json.loads(Path(a.cuestionario).read_text(encoding="utf-8"))
    ev = json.loads(Path(a.evidencia).read_text(encoding="utf-8"))
    n = normalizar(ev)
    aplicadas, sin_match = 0, []
    for slug, prefijo, regla in REGLAS:
        cap = q["capacidades"].get(slug)
        if not cap:
            continue
        hallado = False
        for nivel in ("crawl", "walk", "run"):
            for crit in cap["criterios"][nivel]:
                if crit["texto"].startswith(prefijo):
                    hallado = True
                    if crit["estado"] != "sin_datos":
                        continue
                    r = regla(n)
                    if r is None:
                        continue
                    crit["estado"], crit["evidencia"], crit["confianza"] = r
                    crit["origen"], crit["nube"] = "evidencia_automatica", n["nube"]
                    aplicadas += 1
        if not hallado:
            sin_match.append((slug, prefijo))
    out = a.out or a.cuestionario
    if not a.out:
        Path(out + ".bak").write_bytes(Path(out).read_bytes())
    Path(out).write_text(json.dumps(q, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Nube: {n['nube']}. Propuestas aplicadas: {aplicadas}. Archivo: {out}")
    for s, p in sin_match:
        print(f"AVISO: criterio no encontrado en {s}: {p[:60]}")


if __name__ == "__main__":
    main()
