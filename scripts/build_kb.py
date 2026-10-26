"""Genera kb/capabilities.json y kb/capabilities/<slug>.md desde fuentes/raw/*.txt.
Determinista, sin LLM. Uso: python -I build_kb.py
Texto de madurez en ingles tal como lo publica finops.org (CC BY 4.0).
"""
import json
import re
from pathlib import Path

RAW = Path(__file__).resolve().parent.parent / "fuentes/raw"
KB = Path(__file__).resolve().parent.parent / "kb"
(KB / "capabilities").mkdir(parents=True, exist_ok=True)

SECTIONS = ["Definition", "Maturity Assessment", "Functional Activities",
            "Measures of Success & KPIs", "Inputs & Outputs", "Related Assets"]

def parse(slug):
    lines = [l.rstrip().replace(chr(0x2014), " - ").replace(chr(0x2013), "-")
             for l in (RAW / f"{slug}.txt").read_text(encoding="utf-8").splitlines()]
    bc = next(i for i, l in enumerate(lines) if l.startswith("Framework / Domains /"))
    parts = [p.strip() for p in lines[bc].split("/")]
    domain, name = parts[2], parts[3]
    end = next((i for i, l in enumerate(lines) if l == "On this page" and i > bc), len(lines))
    body = lines[bc + 1:end]
    sec, cur = {}, "Intro"
    for l in body:
        if l in SECTIONS and l not in sec:
            cur = l
            sec[cur] = []
            continue
        sec.setdefault(cur, []).append(l)
    mat = {"Crawl": [], "Walk": [], "Run": []}
    lvl = None
    for l in sec.get("Maturity Assessment", []):
        if l in mat:
            lvl = l
        elif lvl and l.strip():
            mat[lvl].append(l.strip())
    clean = lambda k: [l for l in sec.get(k, []) if l.strip()]
    return {
        "slug": slug, "name": name, "domain": domain,
        "summary": " ".join(clean("Intro")),
        "definition": clean("Definition"),
        "maturity": mat,
        "functional_activities": clean("Functional Activities"),
        "kpis": clean("Measures of Success & KPIs"),
        "inputs_outputs": clean("Inputs & Outputs"),
        "source": f"https://www.finops.org/framework/capabilities/{slug}/",
    }

def md(c):
    o = [f"# {c['name']}", "", f"Dominio: {c['domain']}", f"Fuente: {c['source']} (CC BY 4.0, FinOps Foundation)", "",
         f"Resumen: {c['summary']}", ""]
    for lv in ("Crawl", "Walk", "Run"):
        o += [f"## {lv}", ""] + [f"- {x}" for x in c["maturity"][lv]] + [""]
    o += ["## Actividades funcionales por persona", ""] + [f"- {x}" for x in c["functional_activities"]] + [""]
    o += ["## KPIs y medidas de exito", ""] + [f"- {x}" for x in c["kpis"]] + [""]
    o += ["## Inputs y Outputs", ""] + [f"- {x}" for x in c["inputs_outputs"]] + [""]
    return "\n".join(o)

caps = []
for f in sorted(p for p in RAW.glob("*.txt") if not p.name.startswith("_") and re.fullmatch(r"[a-z0-9-]+", p.stem)):
    c = parse(f.stem)
    caps.append(c)
    (KB / "capabilities" / f"{c['slug']}.md").write_text(md(c), encoding="utf-8")
(KB / "capabilities.json").write_text(json.dumps(caps, ensure_ascii=False, indent=1), encoding="utf-8")
for c in caps:
    m = c["maturity"]
    print(f"{c['slug']:36} {c['domain'][:22]:22} C{len(m['Crawl']):2} W{len(m['Walk']):2} R{len(m['Run']):2} kpi{len(c['kpis']):2}")
print(len(caps), "capacidades")
