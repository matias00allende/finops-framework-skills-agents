# FinOps Maturity Model (Crawl, Walk, Run)

Fuente: https://www.finops.org/framework/maturity-model/ (FinOps Foundation, CC BY 4.0, leída el 2026-10-26). Resumen en español de Chile; las características y metas se citan de forma fiel.

## Principios del modelo

- La práctica de FinOps es iterativa por naturaleza; la madurez de cualquier proceso, actividad funcional, Capability o Domain mejora con la repetición.
- El enfoque "Crawl, Walk, Run" permite empezar pequeño y crecer en escala, alcance y complejidad a medida que el valor de negocio justifica madurar una actividad. Actuar rápido a pequeña escala permite evaluar resultados y descubrir el valor de actuar en forma mayor, más rápida o más granular.
- Las designaciones sirven para identificar dónde se opera hoy y qué áreas pasar de Crawl a Walk o de Walk a Run.
- Son guías generales: la meta nunca debe ser simplemente alcanzar "Run" en cada Capability.
- Ejemplo de la fuente: una organización con anomaly detection en etapa Walk que ha sido adecuada para los pocos picos de costo vividos debería invertir en otras Capabilities con beneficio inmediato; el esfuerzo en una Capability que ya cumple su medida de éxito no aporta beneficio.
- Estar en Walk no es bueno ni malo en sí; hay que enfocarse menos en llevar todo a Run y más en los resultados de negocio o tecnología que busca la Capability. Priorizar madurar las Capabilities con mayor valor de negocio.
- Cada Capability y actividad funcional puede estar en un nivel distinto. Existe el FinOps Assessment (ver assessment.md) y esta rúbrica sirve de atajo de comunicación.

## Crawl

Maturity Level Characteristics:
- Very little reporting and tooling
- Measurements only provide insight into the benefits of maturing the capability
- Basic KPIs set for the measurement of success
- Basic processes and policies are defined around the capability
- Capability is understood but not followed by all the major teams within the organization
- Plans to address "low hanging fruit"

Sample goals/KPI from the FinOps Community (data.finops.org):
- Able to allocate at least 70% of cost to known owner
- Commitments discount target coverage of approximately 60%
- Forecast spend to actual spend accuracy variance is below 20%

## Walk

Maturity Level Characteristics:
- Capability is understood and followed within the organization
- Difficult edge cases are identified but decision to not address them (informed ignoring) is adopted
- Automation and/or processes cover most of the Capability requirements
- Most difficult edge cases (ones that threaten the financial well-being of the organization) are identified and effort to resolve has been estimated
- Medium to high goals/KPIs set on the measurement of success

Sample goals/KPI from the FinOps Community (data.finops.org):
- Able to allocate at least 85% of cost to known owner
- Commitments discount target coverage is greater than 75%
- Forecast spend to actual spend accuracy variance is less than 10%

## Run

Maturity Level Characteristics:
- Capability is understood and followed by all teams within the organization
- Difficult edge cases are being addressed
- Very high goals/KPIs set on the measurement of success
- Automation is the preferred approach

Sample goals/KPI from the FinOps Community (data.finops.org):
- Greater than 90% of spend can be allocated
- Commitment discount target coverage is greater than 80 (la fuente no incluye el signo %)
- Forecast spend to actual spend accuracy variance is less than 5%

## Resumen comparativo de metas numéricas

| Métrica | Crawl | Walk | Run |
|---|---|---|---|
| Costo asignado a un owner conocido | al menos 70% | al menos 85% | más de 90% del gasto asignable |
| Cobertura objetivo de commitment discounts | aprox. 60% | más de 75% | más de 80 (sin unidad en la fuente) |
| Varianza forecast vs gasto real | menor a 20% | menor a 10% | menor a 5% |

Ejemplos por Capability más allá de estas tres métricas: "No publicado en la fuente" (la página solo entrega estas metas de muestra y la característica general por nivel).
