"""Scrape textual (inner_text) de las paginas de capacidades del FinOps Framework.
Salida: fuentes/raw/<slug>.txt. Uso: python -I scrape_raw.py
"""
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "https://www.finops.org/framework/capabilities/"
OUT = Path(__file__).resolve().parent.parent / "fuentes/raw"
OUT.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page()
    pg.goto(BASE, wait_until="networkidle", timeout=60000)
    links = pg.eval_on_selector_all(
        "a[href*='/framework/capabilities/']", "els=>els.map(e=>e.href)")
    slugs = sorted({re.sub(r".*/capabilities/([^/#?]+)/?.*", r"\1", l)
                    for l in links if re.search(r"/capabilities/[^/]+", l)})
    print(len(slugs), slugs)
    slugs = [s for s in slugs if re.fullmatch(r"[a-z0-9-]+", s)]
    for s in slugs:
        pg.goto(BASE + s + "/", wait_until="networkidle", timeout=60000)
        txt = pg.inner_text("main") if pg.query_selector("main") else pg.inner_text("body")
        txt = txt.replace(chr(0x2014), " - ").replace(chr(0x2013), "-")  # regla: solo guion simple
        (OUT / f"{s}.txt").write_text(txt, encoding="utf-8")
        print(s, len(txt))
    b.close()
