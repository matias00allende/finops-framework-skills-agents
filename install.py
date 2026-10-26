"""Instala las skills y el agente FinOps en ~/.claude (o en --destino).

Uso: python -I install.py [--destino <dir .claude>] [--forzar]
Reemplaza el marcador <FINOPS_HOME> por la ruta absoluta de este repositorio. No sobrescribe
archivos existentes salvo con --forzar.
"""
import argparse
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--destino", default=str(Path.home() / ".claude"))
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    destino = Path(a.destino)
    home = AQUI.as_posix()
    n = 0
    for src in list((AQUI / "skills").glob("*/SKILL.md")) + list((AQUI / "agents").glob("*.md")):
        rel = src.relative_to(AQUI)
        out = destino / rel
        if out.exists() and not a.forzar:
            print(f"Existe, se omite: {out}")
            continue
        if out.exists():
            out.with_suffix(out.suffix + ".bak").write_bytes(out.read_bytes())
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(src.read_text(encoding="utf-8").replace("<FINOPS_HOME>", home), encoding="utf-8", newline="\n")
        print(f"Instalado: {out}")
        n += 1
    print(f"{n} archivo(s) instalado(s). Reinicie Claude Code para cargar las skills.")


if __name__ == "__main__":
    main()
