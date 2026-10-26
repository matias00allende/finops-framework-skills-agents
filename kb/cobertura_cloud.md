> Solo la columna AWS tiene recolector en la v1; GCP y Azure son un mapa de trabajo para la v2.

# Cobertura de las 22 capacidades por API de nube

Fuente: matrices internas de verificacion contra documentacion oficial. Nota: cada matriz aplicó un criterio
de clasificación algo distinto (por ejemplo, Allocation es AUTOMATIZABLE en GCP y PARCIAL en AWS), por lo que
los conteos son indicativos.

| Capacidad | AWS | GCP | Azure |
|---|---|---|---|
| Automation, Tools, & Services | SOLO MANUAL | SOLO MANUAL | SOLO MANUAL |
| Executive Strategy Alignment | SOLO MANUAL | SOLO MANUAL | SOLO MANUAL |
| FinOps Assessment | SOLO MANUAL | SOLO MANUAL | SOLO MANUAL |
| FinOps Education & Enablement | SOLO MANUAL | SOLO MANUAL | SOLO MANUAL |
| FinOps Practice Operations | SOLO MANUAL | SOLO MANUAL | SOLO MANUAL |
| Governance, Policy & Risk | PARCIAL | PARCIAL | PARCIAL |
| Intersecting Disciplines | SOLO MANUAL | SOLO MANUAL | SOLO MANUAL |
| Invoicing & Chargeback | PARCIAL | PARCIAL | PARCIAL |
| Architecting & Workload Placement | SOLO MANUAL | SOLO MANUAL | SOLO MANUAL |
| Licensing & SaaS | PARCIAL | PARCIAL | PARCIAL |
| Rate Optimization | AUTOMATIZABLE | AUTOMATIZABLE | AUTOMATIZABLE |
| Sustainability | PARCIAL | AUTOMATIZABLE | PARCIAL |
| Usage Optimization | PARCIAL | AUTOMATIZABLE | AUTOMATIZABLE |
| Budgeting | PARCIAL | AUTOMATIZABLE | PARCIAL |
| Forecasting | PARCIAL | PARCIAL | PARCIAL |
| KPIs & Benchmarking | PARCIAL | PARCIAL | PARCIAL |
| Planning & Estimating | PARCIAL | PARCIAL | PARCIAL |
| Unit Economics | PARCIAL | PARCIAL | PARCIAL |
| Allocation | PARCIAL | AUTOMATIZABLE | PARCIAL |
| Anomaly Management | AUTOMATIZABLE | PARCIAL | PARCIAL |
| Data Ingestion | AUTOMATIZABLE | PARCIAL | AUTOMATIZABLE |
| Reporting & Analytics | PARCIAL | AUTOMATIZABLE | PARCIAL |

- Capacidades con evidencia por API en al menos una nube: 15 de 22.
- Capacidades solo manuales en las tres nubes: 7 (architecting-workload-placement, automation-tools-services, executive-strategy-alignment, finops-assessment, finops-education-enablement, finops-practice-operations, intersecting-disciplines).
- Capacidades automatizables en al menos una nube: 8.
- Ninguna capacidad se cubre al 100 % por API: aun las AUTOMATIZABLES requieren confirmar estrategia, responsables y adopción con evidencia documental o entrevista.