# Tooling, estándares y KPIs de referencia - FOCUS, State of FinOps y biblioteca de KPIs

Fuentes leídas el 2026-10-26 (solo finops.org, focus.finops.org y data.finops.org):
- https://focus.finops.org/ (portada)
- https://focus.finops.org/about-focus/
- https://focus.finops.org/adoption/
- https://focus.finops.org/faqs/ (solo títulos de preguntas visibles; las respuestas están plegadas)
- https://focus.finops.org/docs/use-cases/
- https://focus.finops.org/docs/specification/v1-4/ (solo la portada del documento: estado, abstract y licencia)
- https://www.finops.org/topic/focus/
- https://data.finops.org/ (State of FinOps 2026)
- https://www.finops.org/insights/state-of-finops/ (redirige a data.finops.org; solo título "State of FinOps 2024 Survey Results" visible)
- https://www.finops.org/wg/finops-kpis/ (cinco páginas de la biblioteca)
- https://www.finops.org/framework/maturity-model/ (metas de muestra, ver maturity-model.md)
- https://www.finops.org/framework/technology-categories/

Resumen en español de Chile; términos oficiales en inglés. Lo no encontrado se marca "No publicado en la fuente".

---

## 1. FOCUS (FinOps Open Cost and Usage Specification)

### Qué es
- Especificación abierta que define requisitos para que los generadores de datos de facturación de tecnología produzcan datasets consistentes de costo y uso (topic page de finops.org).
- Definición del documento de especificación: "FOCUS is an open specification for billing data. It defines a common schema for billing data, aligns terminology with the FinOps Framework and defines a minimum set of requirements for billing data." Permite a los practitioners realizar Capabilities comunes (chargeback, cost allocation, budgeting, forecasting, etc.) con un conjunto genérico de instrucciones.
- Portada de focus.finops.org: "The Unifying Language for Technology Value"; normaliza datasets de facturación entre proveedores de AI, cloud, SaaS, data center y otros para reducir la complejidad.
- Licencia del documento: Creative Commons Attribution 4.0 International; política de patentes: Option 4, W3C Mode.

### Versión y estado
- finops.org (topic page) indica "FOCUS is now at version 1.3", con exports nativos de 11+ proveedores (AWS, Microsoft Azure, Google Cloud, Oracle, Alibaba Cloud, otros), un Conformance Program, un Sandbox y biblioteca de use cases y queries.
- focus.finops.org (portada) anuncia "Introducing FOCUS 1.4 - See what's included" y la ruta de la especificación es /docs/specification/v1-4/. Hay por tanto una diferencia entre las dos fuentes (1.3 vs 1.4); prevalece la más reciente del sitio específico de FOCUS (1.4), y la página de Tokenomics de finops.org menciona soporte de costos de IA y tokens en v1.5 (futuro). El detalle del contenido de 1.4 (columnas nuevas): No leído en esta extracción.
- Intención declarada de gobernanza: avanzar hacia un estándar internacional formal.

### Gobernanza (about-focus)
- Iniciativa de especificación abierta de la Linux Foundation, apoyada por FinOps Foundation, Tokenomics Foundation e ITAM Forum. Estructura Joint Development Foundation (JDF) Specification Project, neutral y standalone. Cada release pasa por contribución comunitaria, revisión, aprobaciones, ratificación y revisión de propiedad intelectual, en abierto vía GitHub.
- Steering Committee designado por el Governing Board de la FinOps Foundation (miembros nombrados en la fuente: Ben Olson de Adobe, Casey Doran de IBM Cloudability, Deeja Cruz de Datadog, John Ely de Capital One, Karl Kraft de Walmart, Letian Feng de AWS, Mike Fuller CTO de FinOps Foundation, Sarah McMullin de Google Cloud, Vikram Desai de Microsoft). Hay además Maintainers y Staff.

### Datasets y proveedores (generators) con exports FOCUS (portada, versión indicada por proveedor)
- v1.3: MongoDB, Vercel, Snowflake, Databricks.
- v1.2: AWS, Nebius, Microsoft (Azure), IBM Cloud, Grafana Cloud, STACKIT, Redis, Google Cloud.
- v1.0: Oracle, Alibaba Cloud, Tencent Cloud, Huawei Cloud, OVHCloud, Cloudflare, CoreWeave.
- Los datasets citados en las FAQs: Cost and Usage, Invoice Detail, Billing Period y Contract Commitment (State of FOCUS: "four data sets instead of one" según un activo de la topic page).

### Adopción
- Generators: herramientas y servicios de IA, CSPs (IaaS), vendors SaaS/PaaS, Data Cloud Platforms, ISVs, proveedores de private cloud y equipos internos que hacen chargeback de data center.
- Consumers: FinOps Practitioners.
- Generator + Consumer: vendors de herramientas FinOps.
- Recursos: What is FOCUS? (PDF), paper Adopting FOCUS, FOCUS para data center, FOCUS Sandbox (datos de muestra y consultas SQL), Column Library, curso Intro to FOCUS y certificación Certified FOCUS Analyst.

### Use cases publicados (focus.finops.org/docs/use-cases/), agrupados por Capability
- Allocation: asignar cargos multi-moneda por aplicación; analizar tag coverage; identificar recursos con asignación de costo compartido; track de compras de marketplace entre proveedores; verificar exactitud de facturas de proveedores.
- Anomaly Management: analizar costos por servicio y región; comparar uso de recursos mes a mes; identificar gasto diario anómalo por subaccount, región y servicio; identificar capacity reservations sin uso.
- Budgeting: comparar billed cost por subaccount contra presupuesto; seguir el burn-down de contract commitments; actualizar presupuestos por aplicación.
- Data Ingestion: verificar exactitud de facturas y de cargos; verificar exactitud de descuentos.
- Forecasting: proyectar costos amortizados y cashflow mes a mes según tendencias.
- Governance, Policy & Risk: reportar subaccounts por región.
- Invoicing & Chargeback: reconciliar Cost and Usage con Invoice Detail por Invoice ID; reconciliar liquidación multi-moneda con Lineage IDs; validar variación de impuestos.
- Planning & Estimating: determinar ahorros contratados por moneda virtual; reporte de effective cost de cómputo.
- Rate Optimization: Commitment Discount Coverage Rate con denominador ajustado por elegibilidad; desglose de effective cost de commitment discounts; comparar oportunidades de commitment entre proveedores; efectividad de descuentos por servicio; identificar compromisos sin uso; reportar compras de commitment discounts.
- Reporting & Analytics: analizar costos por SKU, por servicio, por subaccount; calcular unit economics; comparación Cash vs Accrual; determinar Effective Savings Rate (global y por servicio).
- Preguntas frecuentes listadas (FAQs): cómo FOCUS ayuda a reconciliar uso con facturas; por qué los costos FOCUS no coinciden exactamente con la factura; covered y covering charges; cómo medir cobertura de commitments; si se puede usar solo un subconjunto de columnas y seguir conforme; cómo se representan correcciones de facturación; qué pasa al subir de versión; cómo se relacionan conformance y certificación con las versiones. Las respuestas: No leídas (plegadas en la página).

### FOCUS dentro del Framework
- El principio "FinOps data should be accessible, timely, and accurate" dice: "Use FOCUS and other methods to continuously improve normalization, accuracy and consistency in data across technology categories."
- El paper de MCP indica que FOCUS y MCP son complementarios (FOCUS gobierna lo que se gasta; MCP cómo se operacionaliza).

### FOCUS en State of FinOps 2026
- Crecimiento interanual del uso de FOCUS. Principales solicitudes de expansión: cargas de IA, data center y mayor soporte PaaS/SaaS. Las cifras porcentuales de adopción por proveedor no se publican en el texto de la página (están en gráficos): No publicado en el texto.

---

## 2. State of FinOps 2026 (data.finops.org, 6th annual survey)

Encuesta anual de la FinOps Foundation desde 2020. Tamaños de muestra N varían por pregunta (523 a 698 en las preguntas citadas).

Mensajes principales (Executive Summary):
- La misión de la Foundation cambió de "Advancing the People who manage the Value of Cloud" a "Advancing the People who manage the Value of Technology".
- Proactive Technology Value: IA encabeza la agenda; FinOps se mueve "up, left, and out".
- IA: 98% gestiona gasto de IA (31% hace dos años; 63% en 2025). FinOps for AI es la prioridad futura número uno; AI cost management es el skillset número uno a desarrollar. Muchas organizaciones deben autofinanciar la IA con ahorros de optimización.
- Expansión de scope: 90% gestiona o planea gestionar SaaS en el próximo año (65% en 2025, +25), 64% licensing (+15), 57% private cloud (+18), 48% data center (+12); 28% incluye costos de labor.
- Optimización es "table stakes", el valor es la meta: Scopes, Governance/Policy, Organizational Alignment y Forecasting juntos pesan más que optimización sola; rendimientos decrecientes en optimización cloud. Prácticas maduras: unit economics, cuantificación de valor de IA e influencia en selección de tecnología.
- FinOps shifted up: 78% de los equipos reporta al CTO o CIO (+18% vs 2023); reporte al CFO bajó a 8%. Con engagement a nivel VP/SVP/EVP/C-suite se tiene de 2 a 4 veces más influencia en selección de tecnología. Cifras del resumen: selección de servicio cloud 53% vs 12%, selección de proveedor cloud 47% vs 8%, cloud vs data center 28% vs 6%. (La sección Team de la misma página muestra 53% vs 24%, 47% vs 16% y 28% vs 12% para el comparativo "VP+ vs solo Director": la fuente es internamente inconsistente; citar con cautela.)
- Shift left ocurre, pero la medición sigue sin resolverse ("Once you fix it, it's gone"). Pre-deployment architecture costing fue un pedido principal de herramientas.
- Disciplinas que convergen: colaboración más frecuente con ITFM, luego ITAM/SAM, ITSM y ESG; Platform Engineering se suma en shift-left.
- Modelo operativo dominante: enablement centralizado con ejecución federada. 81% opera con centralized enablement (60%) o hub-and-spoke (21%). Equipos lean: organizaciones que gestionan USD 100M+ promedian 8 a 10 practitioners y 3 a 10 contratistas.

Prioridades (multi-select, N=685; % de respondientes, ahora/próximos 12 meses según la tabla): FinOps for AI 33% (sube 6 lugares); aplicar FinOps a más Scopes 28%; workload optimization y waste reduction 25%; AI for FinOps 24% (sube 6); governance y policy a escala 21%; accurate forecasting 20%; unit economics 20% (sube 5); enabling automation 20%; adopción/alineación organizacional 17%; multi-cloud cost reporting 14%; full allocation 14%; architecting for cloud 13%; integrar nueva herramienta FinOps 10%; rate optimization 9%; leadership/executive integration 8%; multi-year investment planning 7%; reporting de carbono 5%; staffing 3%.

Capabilities más priorizadas fuera de cloud (SaaS, Licensing, Data Center, Data Cloud Platforms): Allocation, Forecasting & Budgeting, Planning & Estimating, Data Ingestion y Reporting & Analytics; luego Rate Optimization (SaaS, Licensing, Data Cloud Platforms) o Workload Optimization (Data Center) y FinOps Tools & Services. Conclusión de la fuente: primero visibilidad, luego planificación, luego optimizar por valor.

Top 3 pedidos de herramientas: (1) monitoreo granular del gasto de IA (tokens, solicitudes LLM, utilización de GPU); (2) shift-left, costeo de arquitectura pre-despliegue; (3) "single pane of glass" para distintos tipos de gasto tecnológico. Temas adicionales: remediación automatizada, unit economics técnicas y atribución de valor, adopción de FOCUS en herramientas, forecasting y modelado de escenarios, gestión de licencias ITAM, sostenibilidad junto al costo, allocation compartido y de contenedores.

IA: desafíos principales al aplicar FinOps a IA: visibilidad de costos (precios variables), asignar costos de IA a unidades de negocio y determinar valor/ROI. Importancia de AI for FinOps por encima del punto medio en promedio; casos tempranos listados (ver ai-for-finops.md).

Especificaciones de métricas del resumen de tamaño y KPI propios de la encuesta (ej. gasto cloud medio por tamaño de equipo): presentados en gráficos, "No publicado en el texto".

---

## 3. KPIs de referencia publicados

### 3.1 Metas de muestra por madurez (FinOps Maturity Model, datos de data.finops.org)

| Métrica | Crawl | Walk | Run |
|---|---|---|---|
| Costo asignado a owner conocido | al menos 70% | al menos 85% | más de 90% |
| Cobertura de commitment discounts | aprox. 60% | más de 75% | más de 80 |
| Varianza forecast vs real | menor a 20% | menor a 10% | menor a 5% |

### 3.2 Biblioteca FinOps KPIs (finops.org/wg/finops-kpis/)
- Biblioteca curada por la comunidad, independiente de proveedor cloud, industria, tamaño o madurez. 88 ítems, cinco páginas, última actualización 2026-03-17. Cada KPI tiene definición, fórmula(s), ejemplos y fuentes de datos (el detalle por KPI no fue leído; solo título y descripción de la lista). Metas numéricas por KPI: No publicado en la fuente.
- Filtros: Capabilities relacionadas (Reporting & Analytics, Usage Optimization, Sustainability, Unit Economics, Data Ingestion, Intersecting Disciplines, Rate Optimization, Allocation, KPIs & Benchmarking, Anomaly Management, Budgeting, Licensing & SaaS, Forecasting, Planning & Estimating, Architecting & Workload Placement, FinOps Education & Enablement, Invoicing & Chargeback) y Technology Categories (AI, Data Center, SaaS, Data Cloud Platforms, Licences).

Títulos de KPI identificados (los que el parser alcanzó a separar; la lista puede no ser exhaustiva de los 88):
- Página 1: Value for AI Initiatives; Unified Cost & Usage Visibility; Training Cost Efficiency; Total Unpredicted Variance of Spend; Total Migration Cost Savings; Total Cost of Ownership per Workload; Token Consumption Metrics; Time to First Prompt; Time to Achieve Business Value; Thought Efficiency Index (TEI); Storage Decay Ratio; SaaS Unit Cost; SaaS Optimization ROI; Resource Utilization Efficiency; Redundant Application Coverage Percent; Reasoning Token Ratio; Power Schedule Adherence Rate; Pipeline Jobs Waste; Percentage Variance of Budgeted vs. Forecasted CSP Cloud Spend; Usage or Spend Apportionment Validation.
- Página 2: Percentage Variance of Budgeted vs. Actual CSP Cloud Spend; Percentage Resource Utilization; Percentage of Unallocated Shared CSP Cloud Cost; Percentage of Normalized, Queryable Data within Repository; Percentage of CSP Cloud Costs that are Tagging Policy Compliant; Percentage of Costs Associated with Unallocated CSP Cloud Resources; Percent of Compute Spend Covered by Commitment Discounts; LLM Error Rate; License Utilisation Rate; IT Lifecycle Waste Efficiency.
- Página 3: General Ledger Recharge Rate; Forecast Accuracy Rate (Usage); Forecast (Present) Actual Rate (Carbon); Feature Adoption Rate; Efficiency & Performance ROI; Effective Scan Efficiency; Data Value Density; Data Center Power Usage Effectiveness; Data Center Management Efficiency.
- Página 4: CSP Cloud Budget Burn Rate; CPI Cost Performance Indicator; Cost Visibility Delay; Cost per Thought (LLM Only); Cost per Thought (Full Stack); Cost per Inference; Cost per Gigabytes Stored; Cost per API Call; Cost per Agent Cycle; Consumption versus Commitment; Computational Waste Percentage; Commitment Utilization Score; Carbon Waste / Carbon Efficiency; Carbon per Unit of Cloud Spend; Carbon per Unit of Cloud Service SKU.
- Página 5: Carbon Efficient Locations; Cache Hit Rate; Anomaly Detection Rate; Allocation Accuracy Index (AAI); Active-to-Provisioned User Ratio.

Definiciones textuales relevantes (resumidas de la fuente):
- Percentage Variance of Budgeted vs. Actual CSP Cloud Spend: diferencia entre costos presupuestados y reales por uso de servicios de nube pública.
- Percentage of CSP Cloud Costs that are Tagging Policy Compliant: cumplimiento del tagging; requiere una política de tagging organizacional establecida.
- Percentage of Unallocated Shared CSP Cloud Cost: gastos que no pueden atribuirse directamente a un proyecto, equipo o departamento.
- Percent of Compute Spend Covered by Commitment Discounts: porcentaje del costo de cómputo (excluye Spot) cubierto por commitment discount en el mes anterior.
- Commitment Utilization Score: burndown de capacidad prepagada contra consumo; cerca de 100% indica pronóstico y optimización de tarifas perfectos; valores bajos señalan "shelfware"; sobre 100% revela exposición a tarifas on-demand caras.
- Cost Visibility Delay: tiempo (horas o días) entre que ocurre el costo y su ingesta, normalización y visualización a stakeholders.
- Allocation Accuracy Index (AAI): porcentaje del costo total de infraestructura atribuido directa y correctamente a equipos, proyectos o unidades de negocio.
- Forecast Accuracy Rate (Usage): compara uso pronosticado vs real (vCPUs, memoria, etc.) en un período.
- Computational Waste Percentage: gasto que no dio utilidad de negocio en data cloud platforms (jobs fallidos, recursos ociosos antes de auto-suspensión, sobreaprovisionamiento).
- SaaS Unit Cost, SaaS Optimization ROI y Redundant Application Coverage Percent: desarrollados por el Working Group FinOps for SaaS. Unified Cost & Usage Visibility y Total Cost of Ownership per Workload: desarrollados por el Working Group FinOps for Data Center.
- KPIs de IA: ver sección 10 de ai-for-finops.md.

---

## 4. Tooling

- State of FinOps 2026: expectativas de tooling descritas en la sección 2 (top 3 pedidos y temas adicionales).
- FinOps Landscape (finops.org/landscape/): página enlazada en la navegación, no leída: "No publicado en la fuente" para este documento.
- Vendors de herramientas FinOps como Generator + Consumer de FOCUS: la página de adopción de FOCUS describe el rol pero no lista herramientas específicas en el texto leído.
- Herramientas mencionadas en el paper FinOps for AI: Tools & Services Considerations (listadas a modo de ejemplo en el paper, no recomendaciones oficiales): FinOps-specific (Vantage, CloudZero, Apptio, Pay-i); observabilidad de LLM (Arize Phoenix, LangSmith, Weights & Biases, Helicone, PromptLayer); monitoreo de infraestructura (Grafana, Datadog, Prometheus); AI gateways (OpenRouter, LiteLLM, Kong, Apigee, y ofertas nativas de Amazon Bedrock, Azure AI Foundry y Google Vertex AI).
- Capability asociada en el Framework: Automation, Tools, & Services (Domain Manage the FinOps Practice). Su contenido específico no fue leído en esta extracción.

---

## 5. Technology Categories (finops.org/framework/technology-categories/)

Página leída. Categorías listadas: FinOps for AI, FinOps for SaaS, FinOps for Data Cloud Platforms, FinOps for Data Center y FinOps for Public Cloud. Cada categoría tiene procurement models, pricing constructs, visibilidad de costos y dinámica operativa propios. El detalle por categoría no fue transcrito.
