# finops-framework-skills-agents

Skills y un agente para Claude Code basados en el FinOps Framework 2026 de la FinOps Foundation (CC BY 4.0). Ayudan a evaluar la madurez de una práctica FinOps y a priorizar brechas para mejorarla. Incluye un motor de puntuación determinista y un recolector de evidencia de solo lectura para AWS.

Este proyecto no está afiliado ni respaldado por la FinOps Foundation.

## Qué incluye la versión 1

| Pieza | Para qué sirve | Estado |
|---|---|---|
| Skill `/finops-assessment` | Conduce un assessment en las 4 etapas del Assessment Guide | Usada en un banco de pruebas |
| Skill `/finops-roadmap` | Convierte brechas en una hoja de ruta por horizontes | Depende del resultado del assessment |
| Skill `/finops-ia` | FinOps for AI y AI for FinOps (Tokenomics, Big-T) | Basada en el paper oficial |
| Agente `finops-asesor` | Consultas, assessment y evidencia en AWS | Igual que las skills |
| `scripts/finops_assess.py` | Motor: `init`, `score`, `plan` | Probado con datos sintéticos |
| `scripts/aws_evidencia.py` | Evidencia de solo lectura en AWS | Probado en una cuenta AWS |
| `scripts/mapear_evidencia.py` | Convierte evidencia en propuestas de estado por criterio | 9 pruebas con datos sintéticos |
| `kb/cobertura_cloud.md` | Qué capacidades se pueden medir por API en AWS, GCP y Azure | Investigación basada en documentación oficial, sin verificación mediante código |

## Qué queda para la versión 2

Lo siguiente no se publica porque no se pudo comprobar de punta a punta:

- Recolectores de GCP y Azure. Se escribieron según la documentación oficial y se probaron solo con simulaciones; en GCP se comprobaron además dos llamadas (Budget API y Recommender) contra una cuenta real, pero los bloques que dependen del export de facturación a BigQuery no tuvieron datos.
- Generador de informes DOCX o PPTX.
- Extensión de los recolectores a varias cuentas, suscripciones o proyectos.

Estas funciones no están disponibles en el repositorio. La matriz `kb/cobertura_cloud.md` queda como mapa de trabajo para esa versión.

## Instalación

```
git clone https://github.com/matias00allende/finops-framework-skills-agents
python -I finops-framework-skills-agents/install.py
```

`install.py` copia las skills y el agente a `~/.claude`, reemplaza el marcador `<FINOPS_HOME>` por la ruta del clon y no sobrescribe archivos existentes salvo con `--forzar`. Requiere Python 3.10 o superior. Después, reinicie Claude Code.

El texto del framework no se redistribuye. Antes del primer uso, genérelo en su equipo:

```
pip install -r requirements.txt
playwright install chromium
python -I scripts/scrape_raw.py
python -I scripts/build_kb.py
```

Eso descarga las páginas públicas de finops.org y crea `kb/capabilities.json` y `fuentes/raw/`, ambos ignorados por git. Si falta `kb/capabilities.json`, el motor se detiene con un mensaje que explica qué ejecutar.

## Uso

```
python -I scripts/finops_assess.py init --scope "<nombre>" --out <ruta>/cuestionario.json [--caps slug1,slug2]
python -I scripts/aws_evidencia.py --profile <perfil> --tag-key <clave_tag> --months 3 --out <ruta>/evidencia.json
python -I scripts/mapear_evidencia.py <ruta>/cuestionario.json <ruta>/evidencia.json
python -I scripts/finops_assess.py score <ruta>/cuestionario.json --json <ruta>/resultado.json --out <ruta>/informe.md
python -I scripts/finops_assess.py plan <ruta>/resultado.json --top 5
```

También puede pedirlo en lenguaje natural: `/finops-assessment`, `/finops-roadmap`, `/finops-ia` o el agente `finops-asesor`. El mapeador solo propone estados; una persona los confirma.

Estados de criterio: `cumple`, `parcial`, `no`, `na`, `superado`, `sin_datos`. Los criterios describen el estado de cada nivel y no son requisitos acumulativos.

## Cómo se calcula el nivel

Es una heurística propia, no el puntaje oficial. El nivel de una capacidad es el más alto cuyos criterios aplicables se cumplen en al menos 75 %. Si menos del 50 % de los criterios tiene evidencia, la capacidad se marca "No concluyente" y queda fuera de promedios, brechas y plan. El puntaje oficial del Assessment Guide es el de los 5 lentes (Knowledge, Process, Metrics, Adoption, Automation, escala 0-4), que el motor también admite.

## Seguridad

- `aws_evidencia.py` solo lee: Cost Explorer, Budgets, Data Exports, CUR y Compute Optimizer. Los permisos mínimos están en su docstring. No use `ce:*`, porque incluye escrituras.
- Use un rol o usuario de solo lectura, no una cuenta de administración.
- Los cuestionarios y la evidencia pueden contener identificadores de su organización. Guárdelos fuera de este repositorio; el `.gitignore` excluye `evidencia*.json`, `cuestionario*.json`, `resultado*.json` e `informe*.md`.
- Guarde los artefactos de cada organización en `clientes/` o `salidas/` (ignorados por git) o fuera del clon.
- No incluya datos personales ni RUN en un cuestionario.

## Solución de problemas

| Síntoma | Causa | Acción |
|---|---|---|
| El motor se detiene pidiendo `kb/capabilities.json` | No se generó el KB local | Ejecute `scrape_raw.py` y luego `build_kb.py` |
| `build_kb.py` falla con StopIteration | Una página sin el encabezado esperado | Repita `scrape_raw.py` y revise el archivo |
| `scrape_raw.py` encuentra menos de 22 capacidades | finops.org cambió su estructura | Ajuste el selector |
| UnicodeEncodeError en consola de Windows | Codificación cp1252 | Anteponga `PYTHONIOENCODING=utf-8` |
| % asignado bajo con el tag bien aplicado | El tag no está activado como cost allocation tag | Revise `allocation_tag_coverage.activacion` en la evidencia |
| Capacidad "No concluyente" | Menos de 50 % de criterios con evidencia | Complete la entrevista y la evidencia; "No concluyente" no equivale a un nivel inicial |
| Nivel bajo en una organización madura | Criterios de Crawl marcados `no` | Márquelos `superado` |

## Limitaciones conocidas

- Las fases Inform, Optimize y Operate no se publican por capacidad en finops.org; no se asignaron.
- Los criterios Crawl/Walk/Run están en inglés, como los publica la fuente; las skills los traducen al presentar.
- El cuestionario oficial de Discovery no es público, así que no se reproduce.
- FOCUS: finops.org indica la versión 1.3 y focus.finops.org anuncia la 1.4. Verifique antes de citar.
- La evidencia automática de AWS cubre 12 criterios; el resto requiere entrevista o documentos.
- Ninguna capacidad se cubre al 100 % por API: estrategia, responsables y adopción requieren evidencia documental.

## Decisiones de diseño

- Texto crudo con Playwright en lugar de WebFetch, porque WebFetch devuelve resúmenes de un modelo auxiliar y alteraba umbrales numéricos.
- Motor determinista sin LLM: el puntaje debe ser reproducible y auditable.
- Dos modos de puntaje (criterios y lentes): los criterios dan acciones concretas; los lentes siguen la metodología oficial.
- Recolectores con la biblioteca estándar y credenciales externas: sin credenciales almacenadas.

## Licencia

MIT para el código, las skills y el agente (archivo `LICENSE`). Atribución del framework en `NOTICE.md`.

## Autor

Matías Allende
[LinkedIn](https://www.linkedin.com/in/matiasallende/) · matias.allende.contreras@gmail.com
