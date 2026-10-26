# AI for FinOps y FinOps for AI - síntesis de fuentes oficiales

Todas las fuentes son de finops.org (FinOps Foundation, CC BY 4.0 salvo indicación) y fueron leídas el 2026-10-26. Resumen en español de Chile; términos oficiales en inglés. Lo que la fuente no publica se marca "No publicado en la fuente".

## 0. Distinción de conceptos (según la fuente)

- FinOps for AI (o AI Value): gestionar el costo y el valor de las inversiones en IA.
- AI for FinOps: usar IA (Generative y Agentic) para que la propia práctica FinOps sea más rápida, precisa y escalable.
- AI Tokenomics: disciplina de convertir energía y capital en capacidades de IA y consumir esa inteligencia con eficiencia para obtener valor medible. Tres etapas: production, consumption (selección de modelo, routing, caching, forecasting) y value. Cubre el costo total de la IA, no solo tokens. Dentro del Framework, Tokenomics está junto a AI Value y AI for FinOps. FOCUS v1.5 agregará soporte para costos de IA y tokens (según la página de Tokenomics; la página de FOCUS en focus.finops.org habla de 1.4: ver tooling-estandares.md).

## 1. URLs leídas

Leídas con contenido:
- https://www.finops.org/topic/ai-for-finops/
- https://www.finops.org/topic/ai-tokenomics/
- https://www.finops.org/topic/ai-value/
- https://www.finops.org/insights/ai-for-finops-agentic-use-cases/
- https://www.finops.org/wg/model-context-protocol-mcp-ai-for-finops-use-case/
- https://www.finops.org/wg/managing-ai-value-finops-practice-operations/
- https://www.finops.org/wg/finops-for-ai-tools-services-considerations/
- https://www.finops.org/wg/ai-finops-prompts/
- https://www.finops.org/assets/big-t-notation/
- https://www.finops.org/wg/finops-kpis/ (paginada, 5 páginas leídas)
- https://data.finops.org/ (State of FinOps 2026, sección AI)

Leídas pero sin texto útil (solo reproductor de video incrustado; se usó únicamente la descripción de la página de tema):
- https://www.finops.org/assets/ai-for-finops-primer-from-generative-ai-to-agentic-automation/
- https://www.finops.org/assets/ai-for-finops-from-hype-to-helpful/
- https://www.finops.org/assets/onboarding-your-ai-hire-a-finops-foundation-playbook/
- https://www.finops.org/assets/from-specialist-bottleneck-to-ai-powered-scale/

Fallidas o vacías:
- https://www.finops.org/assets/the-five-layer-tokenomics-stack/ (HTTP 404)
- https://www.finops.org/assets/turning-ai-cost-data-into-strategic-decision-insights/ (sin contenido)
- https://www.finops.org/assets/from-reactive-to-autonomous-finops-agentic-ai-rightsizing-at-sp-global/ (sin contenido)

## 2. AI for FinOps (topic principal)

- 81% de los practitioners de la encuesta State of FinOps 2026 califica la IA como herramienta de productividad importante dentro de su práctica.
- Casos de uso tempranos listados: anomaly detection y alertas más rápidas; recomendaciones automáticas de right-sizing; consulta de datos de costo en lenguaje natural; compra automatizada de instrumentos de descuento; etiquetado de recursos para acelerar el allocation.
- Estándares como Model Context Protocol (MCP) permiten que agentes de IA se conecten directo a APIs de billing cloud, herramientas de cost management y fuentes de datos FinOps, convirtiendo preguntas en lenguaje natural en análisis de costo en tiempo real sin integración a medida.
- Hipótesis de la fuente: AI for FinOps puede seguir el camino de otras herramientas FinOps (ventaja para equipos avanzados, luego estándar). Con 81% de equipos operando con modelos lean y de enablement centralizado, la IA permite escalar sin headcount, amplificando y no reemplazando la experticia.

Lecturas clave (Must Reads) del topic: AI for FinOps: Agentic Use Cases in FinOps; MCP: An AI for FinOps Use Case; AI for FinOps Primer: From Generative AI to Agentic Automation; Managing AI Value Using FinOps Practice Operations.

Otros activos listados en el topic (solo título y descripción de portada): Big-T Notation (2026-08-10); The Five-Layer Tokenomics Stack (2026-08-10: "What AI costs is decided in the lower layers. How much AI spend is decided in the upper ones"); From Specialist Bottleneck to AI-Powered Scale (J.C. Griffin, Grainger, 2026-08-24: los dashboards solo funcionan si la gente va a ellos); Onboarding Your AI Hire: A FinOps Foundation Playbook (Mike Fuller y Rob Martin, 2026-07-27: tratar a un agente de IA como un nuevo contratado, con rol, curva de confianza y accountability); From Reactive to Autonomous FinOps: Agentic AI Rightsizing at S&P Global (Anuthama Chandrasekaran, 2026-07-20: gasto AWS de USD 2.000 millones; pasó de right-sizing manual por correo, cerca de una hora de ingeniero por instancia, a un flujo agentic que razona la recomendación, revisa historial de CPU y red y crea el ticket de cambio).

## 3. Casos de uso agentic (Insights: Agentic Use Cases in FinOps)

1. Natural Language Dashboards y reconciliación financiera: agentes que leen datos crudos (Excel de presupuestos, forecasts trimestrales), comparan gasto real contra presupuesto aprobado, detectan desvíos sobre umbrales y generan dashboards a demanda; informes delta entre varios proveedores.
2. Autonomous Waste Discovery: el agente investiga el recurso subutilizado, encuentra tags o IDs, identifica al owner y crea y asigna un ticket (ej. Jira) para clusters de caché subutilizados o recursos huérfanos. Un equipo redujo la investigación inicial de 15 minutos por ticket a prácticamente cero. Implementaciones avanzadas usan un "orchestrator agent" con semantic routing hacia "consultant agents" (governance engine, cost anomaly detector, tagging policy expert).
3. Proactive Guardrails en CI/CD (shift-left): agentes en pull requests revisan la configuración contra guardrails FinOps antes del despliegue.
4. Personalized Outreach y Gamification: mensajes personalizados por Slack al último usuario que interactuó con un servicio (datos de CloudTrail). Un practitioner reportó 40% casi 50% de tasa de acción sobre los mensajes; se puede notificar a gerentes cuando un miembro ahorra dinero.
5. Security Score Improvement: agentes que crean PRs que corrigen hallazgos de seguridad cloud.
6. Contextual Resource Labeling: inferir etiquetas de recursos sin tag analizando cuándo corren y con qué servicios se conectan, para showback.
7. Candidate and Management Fit: uso inesperado de un agente para evaluar candidatos de traslado interno (caso de una gerente en un banco LATAM).

Implicancias señaladas:
- El rol pasa de "doing the work" a "orchestrating the workers"; el valor del practitioner estará en definir guardrails y objetivos de los agentes.
- Trust gap: la mayoría de las organizaciones aún no permite a agentes hacer cambios en producción ni borrar recursos sin aprobación humana; los agentes son co-diseñadores o companions. La verificación sigue siendo crítica por las inexactitudes de los modelos ("slop").
- Innovation Value Paradox: la exigencia de NPV positivo puede frenar la experimentación. Recomendación: financiar iniciativas por períodos más cortos con revisiones más frecuentes y relajar requisitos de business case en etapas tempranas.
- Nueva unit economics: "cost per thought" o "token use budgeted" por proyecto; el costo de API de los agentes es tan importante como el del cómputo subyacente.
- Transición de "agent-assisted" a "agent-executed" requiere procesos de change management.

## 4. MCP como caso de uso (Working Group paper)

Resumen de la fuente: MCP es un estándar abierto ("USB-C de las aplicaciones de IA") para integrar datos, herramientas y recursos cloud con modelos generativos; reduce alucinaciones y mejora la precisión de recomendaciones de optimización.

Beneficios: respuestas con contexto actual del CSP, acceso a documentación viva, integración de flujos (CDK, Terraform, CLI), alineación de dominio, discovery de tools y agentes.

Desventajas técnicas: ventana de contexto limitada (cada conexión MCP consume parte), autenticación fragmentada (OAuth, API keys, sesión), dificultad para segregar scopes (la lista de tools se entrega a todos los clientes), overhead de integración, cumplimiento y gobernanza (HIPAA, GDPR).

Consideraciones FinOps: el contexto adicional aumenta el conteo de tokens y el costo; MCP no resuelve todo (difícil correlacionar uso con cost drivers sin tagging, logging y atribución); visibilidad entre equipos; trade-off latencia vs costo.

Riesgos de seguridad citados: RCE (CVE-2025-49596 en MCP Inspector), robo de tokens y secuestro de sesión, prompt injection y suplantación de tools, compromiso de servidor MCP ("keys to the kingdom"), control de acceso y permisos insuficientes (se requieren capas externas de control).

Beneficios FinOps de MCP: Context Modularity, Tooling Governance, Prompt Reuse & Cost Attribution, Environment Control. Ejemplo de gobierno: exponer solo agentes aprobados según costo estimado por invocación, benchmarks de exactitud, políticas del departamento y validación de seguridad y cumplimiento (ej. residencia de datos). Relación con FOCUS: FOCUS gobierna "lo que gastamos"; MCP gobierna "cómo ese gasto se operacionaliza mediante contexto y acción".

Siete casos de uso con prompts de ejemplo: (1) Automated Cost Analysis & Anomaly Detection; (2) Scenario Modeling & Cost Impact Simulations; (3) Cost Estimation from Business Requirements; (4) Scaling & Unit Economics Analysis; (5) Multi-Stakeholder FinOps Reporting; (6) Proactive Budget Guardrails (ej. bloquear un deploy de Terraform si el costo mensual estimado supera USD 5.000); (7) Tagging & Cost Allocation Enforcement.

Arquitectura: MCP Client, MCP Host (autenticación, balanceo, observabilidad, metering para FinOps, gobierno central), además de servidores y recursos (el texto leído detalla Client y Host; el resto de componentes: No leído en esta extracción).

## 5. Prompts y buenas prácticas (AI for FinOps Fundamentals: Use Cases and Prompt Practices, actualizado mayo 2026)

- La calidad del contexto importa más que la redacción del prompt (integraciones, RAG, MCP, exports estructurados o reportes pegados).
- Cuatro modos de asistencia de IA: Inform & explain; Analyze & detect; Recommend; Act & automate (este último requiere herramientas a medida o infraestructura agentic).
- Relación con madurez: Crawl = modos de bajo riesgo (inform, summarize, draft); Walk = analizar y recomendar con validación humana; Run = casos agentic con circuit breakers, límites de iteración y revisión humana antes de ejecutar. Usar enfoques agentic sin tagging, atribución y gobernanza sólidos produce resultados poco confiables.
- Human-in-the-loop innegociable en decisiones consecuentes; validar contra fuentes primarias (AWS Cost Explorer, Azure Cost Management, Google Cloud Billing); pedir al modelo que verifique si siguió todos los pasos; usar otros agentes para evaluar.
- Estructura de cada caso: Prompt Title y descripción, FinOps Capability, FinOps Persona(s), AI Assistance Mode, Expected Outcome, Context, Prompt, Customization Notes, Indicators of Success.
- Casos incluidos (títulos publicados): Identify Optimization Opportunities from a Resource Utilization Report (Usage Optimization); Identifying Data Quality Gaps in Cloud Cost and Usage Ingestion (Data Ingestion); Summarize and explain a cost anomaly for stakeholder communication; Generate an Executive Summary from a FinOps Maturity Assessment; Analyze Budget Performance and Support Adaptive Budget Planning; Identify workloads running on deprecated VM Family types and expiration date of commitments; Build and Validate a Technology Spend Forecast from Historical Usage and Planned Changes; Draft FinOps Policy Text from Business Priorities, Technology Strategy, and Constraints; Recommendations for forecasting and communicating realized value. Capabilities mapeadas observadas: Usage Optimization, Data Ingestion, Reporting & Analytics, Allocation, FinOps Practice Operations (y otras en los casos restantes: el mapeo completo por caso no fue extraído).

## 6. Capacidades (Capabilities) afectadas por la IA

Según las fuentes leídas (no hay una tabla única publicada con este título; esto es una compilación):
- FinOps Practice Operations: mayor volumen y velocidad de proyectos de IA, personas nuevas (data scientists, ML engineers); necesita AI Investment Council, ownership claro, funding incremental.
- Allocation y Data Ingestion: etiquetado de recursos de IA, atribución de costo por modelo, equipo, aplicación; gateways que registran metadatos de cada llamada.
- Reporting & Analytics, Anomaly Management: seguimiento granular a nivel de token o GPU; alertas de picos.
- Forecasting, Budgeting, Planning & Estimating: cargas impredecibles; presupuestos con umbrales y revisión frecuente.
- Unit Economics y KPIs & Benchmarking: costo por inferencia, por thought, por caso de uso; ROI.
- Usage Optimization y Rate Optimization: model routing, caching, utilización de GPU, reservas.
- Architecting & Workload Placement: clase de complejidad de tokens (Big-T), build vs buy.
- Governance, Policy & Risk: AI Investment Council, guardrails, tope de gasto.

## 7. Managing AI Value Using FinOps Practice Operations (actualizado 2026-02-23)

Desafíos: alto volumen de proyectos simultáneos; velocidad de desarrollo y poco tiempo de decisión; novedad e inexperiencia en gestionar y pronosticar; atención de toda la organización incluida la alta dirección; diversidad de quienes construyen con IA, fuera de Engineering tradicional.

Mejores prácticas recomendadas:
1. Establecer ownership y accountability (por equipo, proyecto o departamento).
2. Rastrear y analizar costos; etiquetar recursos de IA; decidir si importa desempeño, costo o ambos.
3. Colaborar y comunicar; incluir data scientists y ML engineers.
4. Fijar umbrales de plan y presupuesto para proyectos de IA (inicialmente a nivel empresa para aislar gastos descontrolados); ajustar en períodos de entrenamiento o pruebas.
5. Fund Incrementally: cuanto menos predecible el proyecto, más frecuente la revisión; no dar meses de presupuesto cuando el forecast solo es confiable por semanas; mentalidad fail-fast.
6. Usar las herramientas correctas: dashboards, alertas, hard-spend caps visibles.
7. Desarrollar nuevas habilidades.
8. Pasar de gestión reactiva a proactiva.
9. Nuevas formas de medir costos: GPU, costo por modelo o tarea (ej. cost per AI prediction); Unit Economics para comparar inversiones de IA.
10. Eficiencia en AI Ops y plataformas: uso eficiente de GPU, tamaño de clusters, recursos más baratos; FinOps integrado en procesos de los equipos de IA.
11. Usar IA para mejorar FinOps (con humanos por la alta varianza y no determinismo).
12. Medir el valor de negocio (consistencia en atar costo a valor; KPIs exigidos a proyectos de IA).

AI Investment Council (equipo tipo Tiger Team):
- Propósito: identificar y evaluar oportunidades de inversión responsable y de alto impacto; asesorar sobre portafolio, riesgo y tendencias; alinear con misión, estándares éticos y sostenibilidad.
- Principios: Strategic (alineado al negocio, "move fast spend intentionally"), Disciplined ("every AI dollar has an owner"), Responsible (ético y conforme, "start small, prove value, and then scale"), Future-ready.
- Rol de FinOps: supervisión financiera de infraestructura cloud, costos de training e inferencia, servicios de terceros, presupuestos de experimentación; AI ROI & Value Measurement (cost-to-value ratios, payback periods); Cost Transparency & Chargeback (showback/chargeback); guía de optimización y escalabilidad (atribución de plataformas compartidas y foundation models); input de riesgo y cumplimiento (rightsizing entrenamiento vs inferencia, trade-offs de modelos). Debe ser socio estratégico involucrado temprano, maximizando el valor de la IA y no minimizando la ambición.
- Integrantes sugeridos: Business/Product owners; AI/Technology Lead; Enterprise Architecture; equipos de plataforma de IA; líderes de infraestructura; IT Security/Risk; Finance e IT Finance; FinOps Leads; Procurement. Presidido idealmente por un C-level o ejecutivo senior.
- Revisión requerida cuando: una nueva iniciativa pide fondos incrementales; un piloto busca escalar; el gasto supera umbrales; se introducen servicios de costo variable. Experimentación de bajo costo bajo umbrales puede avanzar sin revisión.
- Cadencia: según demanda; muchas organizaciones se reúnen mensualmente; algunas revisan decenas de solicitudes y se reúnen con más frecuencia y sesiones más breves.
- Objetivo de las revisiones: información consistente, KPIs y metas comunes, gasto real vs esperado, señales de valor, riesgos de costo y anomalías, acciones de optimización; financiar los siguientes pasos y no proyectos completos; no debatir detalles de arquitectura.
- Éxito: inversiones con valor claro o aprendizaje rápido; visibilidad de costo y patrones predecibles; decisiones de escalar basadas en datos.
- Charter de ejemplo: secciones Objectives, Council Membership/Personas, Meetings, Investment Principles, Process for Interacting with AI Investment Council (contenido desplegable no extraído).

## 8. Herramientas y servicios de IA (FinOps for AI: Tools & Services Considerations, 2026-04-23)

Principio: los costos de IA se componen (compounding); sobreaprovisionar en IA genera estructuras de costo multiplicativas; un entrenamiento mal gestionado, un endpoint sin throttling o un agente en loop pueden crecer exponencialmente en horas.

Ciclo de vida de IA y consideraciones FinOps:
- Training: la fase de mayor cómputo. Entrenar un foundation model puede costar USD 5M a 100M+; el default para la mayoría es un modelo gestionado vía API. Palancas: spot/preemptible con checkpointing (reducción de 60 a 80% del cómputo), mixed precision, monitoreo de utilización de GPU (un cluster al 40% desperdicia más de la mitad del gasto).
- Tuning/Augmentation: LoRA y PEFT; antes de afinar, agotar prompt engineering; considerar costo de preparación y etiquetado de datos, frecuencia de reentrenamiento e infraestructura de serving.
- Model-level optimization: quantization, distillation, pruning, Mixture-of-Experts, speculative decoding. Model routing o cascading puede reducir el costo promedio de inferencia entre 60 y 80% en cargas mixtas.
- Caching: prompt caching (puede reducir 50 a 90% el costo de la porción cacheada de entrada), semantic caching, KV cache. Un hit rate de 10% puede no justificar la capa; 60% casi seguro sí.
- Evaluación y QA: la inversión en evaluación suele costar menos que las fallas de calidad que evita; la regresión automatizada es un control de costo.
- Inference: es donde la mayoría gasta más y donde están más palancas; continuous batching; preguntar por throughput y no solo latencia; comportamiento de autoscaling.
- Vector databases y RAG: costos subestimados (embeddings, almacenamiento, mantenimiento de pipeline); para bases pequeñas y estáticas puede bastar búsqueda por keywords o contexto largo.
- AI Gateway: valioso con tres o más modelos o proveedores; registrar cada llamada con metadatos (equipo, aplicación, modelo, tokens de entrada y salida) es la base de la asignación de costos; exigir guardrails de presupuesto.
- Hardware: ajustar la clase de GPU a la carga (no pedir H100 para lo que corre en L40S o A10G); on-demand puede costar 2 a 3 veces el reservado a 1 o 3 años; reservar la línea base y usar on-demand/serverless para picos; autoscaling a cero en inferencia.
- Agent frameworks: los costos se vuelven impredecibles rápido; una interacción puede generar 5, 10 o 50 llamadas al modelo; límites máximos de iteración y controles de presupuesto no son opcionales; exigir trazabilidad y atribución de costo por ejecución de agente.
- Observabilidad: no negociable. Métricas que exigir: cost per use case, desglose de tokens (input vs output, cached vs uncached, por modelo), utilización de GPU, tasas de error y reintentos.
- Data pipelines y feature stores: procesamiento incremental; el costo de storage de IA puede rivalizar con el de cómputo; atención al re-embedding.
- Dónde aparecen los costos: servicios cloud directos, suscripciones SaaS, marketplace, SKUs en acuerdos empresariales, reportes de gastos (shadow IT).
- Build vs Buy vs Managed: el managed tiene mayor costo unitario pero menor TCO con capacidad de ingeniería limitada. Ejemplo: un vector DB self-hosted que ahorra USD 500 al mes puede costar USD 5.000 al mes en tiempo de ingeniería.
- Use case economics (unidad real de medida): costo por consulta de cliente resuelta, por documento resumido, por code review, por llamada de ventas analizada. Ejemplo textual: resolver 200.000 consultas a USD 0,25 promedio, bajando de USD 0,40 el trimestre anterior.
- AI Tool Lifecycle Management: al aprobar y revisar, verificar Visibility, Accountability, Optimization cadence y Exit criteria.

## 9. Tokenomics y notación Big-T

Fuente: Big-T Notation, creada por Dan Neff (Adobe), publicada por la Tokenomics Foundation (2026-08-10). Marco abierto y neutral; informal, sin pruebas formales, es una herramienta de pensamiento.

- Notación: T(n * k * a) = requests (o tamaño de input) x model calls por request x agent depth.
  - n: requests o tamaño de entrada.
  - k: llamadas al modelo por request (suele ser invisible: pasos de razonamiento, cadenas multi-turno, tool calls que reenvían contexto).
  - a: agent depth (sub-agentes llamando sub-agentes).
- Preguntas en orden: primero, qué clase tiene la carga (decisión de arquitectura); segundo, qué tan barato corre dentro de su clase (compresión, routing, caching, serialización).
- Escalera de complejidad:
  - T(1) constante: no se llama al modelo por request (cache hit, lookup estático, embedding search). Fix: cachear y precomputar.
  - T(log n) sublineal: código determinista reduce el input antes del modelo (RAG bien hecho). Resultados publicados: vistas SQL que reducen datos clínicos de cerca de 240.000 tokens a 19.000; pipelines de recuperación que eliminan más de 99,9% de un corpus de un millón de tokens.
  - T(n) lineal: una llamada por request; el default saludable. Vigilar overhead fijo por catálogos grandes de tools.
  - T(n*k) multiplicativo: k llamadas por request; el razonamiento extendido puede consumir más de cien mil tokens por request produciendo unos cientos visibles; herramientas no componibles que reenvían contexto pueden costar 10 a 20 veces la versión compuesta.
  - T(n*k*a) agent-multiplicative: el "O(n al cuadrado) de la IA"; fix: acotar profundidad, circuit breakers y presupuestos.
  - T(infinito) unbounded: loops sin condición de término; fix: condiciones de término duras y circuit breakers.
- Pregunta única: ¿cuál es la clase de complejidad de tokens de esta carga y está justificada por el valor que produce?
- Ejemplo trabajado: resumir diez white papers de cuatro formas, mismo piso de calidad, aproximadamente 34 veces de diferencia (más de 97% de reducción): T(n*k) USD 3,04; T(n) USD 0,65; T(n) USD 0,13; T(n) USD 0,09. Palancas: aislar contextos, dimensionar el modelo correcto, acotar la salida con plantillas.
- Comparación de enfoques: llamadas estándar (línea base, T(n*k)); modo de generación de código (cerca de 80% menos tokens, T(n)); recuperación filtrada (92 a 99,9% de reducción, T(log n)).
- Cinco palancas: (1) Model routing; (2) Prompt engineering y serialización (formatos compactos pueden usar cerca de la mitad de los tokens); (3) Caching como principio de diseño (prompt-prefix y semantic); (4) Abstraction transparency (créditos y licencias por asiento ocultan la economía de tokens); (5) Workload classification & governance.
- Paradoja de Jevons: los precios por token bajan pero el consumo total explota.
- Cómo usarlo: visibilidad primero (instrumentación antes de optimización); clasificar las cargas de mayor gasto; hacer la pregunta única; cambiar la clase donde la arquitectura lo permita; optimizar dentro de la clase y luego gobernar.
- The Five-Layer Tokenomics Stack: la página oficial devolvió 404. Según la descripción en el topic: lo que cuesta la IA se decide en las capas inferiores (L1 silicon a L5) y cuánto se gasta en las superiores. La página de Tokenomics menciona además "The Seven-Layer Tokenomics Stack" publicado por el grupo de trabajo: No leído.
- Datos del State of Tokenomics (septiembre 2026, encuesta a 472 organizaciones, según la página de Tokenomics): 43% nombra demostrar valor o ROI como principal desafío y casi tres de cuatro no pueden conectar con confianza el gasto de IA con un resultado que su CFO aceptaría.

## 10. Métricas de costo de IA publicadas

De la biblioteca oficial FinOps KPIs (https://www.finops.org/wg/finops-kpis/, 88 ítems, última actualización 2026-03-17; fórmulas y ejemplos están en el detalle de cada KPI, que no se leyó):
- Token Consumption Metrics: costo de modelos basados en tokens según uso de tokens de entrada y salida; facilita prompt engineering.
- Cost per Inference: costo de una inferencia individual (chatbots, recomendadores, reconocimiento de imágenes); eficiencia operativa de modelos desplegados.
- Cost per Thought (LLM Only): costo de inferencia LLM autocontenida, sin infraestructura, por request de IA (estimación de SDK con conteo de tokens x precio del modelo).
- Cost per Thought (Full Stack): costo completo por request de IA de extremo a extremo, incluida la infraestructura.
- Cost per Agent Cycle: costo de un ciclo de razonamiento de agente (excluye cargas de una sola llamada).
- Cost per API Call: costo promedio por llamada a servicios de IA gestionados (ej. SageMaker, Vertex AI).
- Reasoning Token Ratio: costo por token de salida; un ratio creciente sube el costo por token aunque el volumen sea plano.
- Cache Hit Rate: porcentaje de tokens servidos desde caché; un valor bajo señala oportunidad.
- LLM Error Rate: tasa de llamadas LLM fallidas; proxy del desperdicio por reintentos.
- Thought Efficiency Index (TEI): índice compuesto de qué tan eficientemente una aplicación convierte llamadas LLM en trabajo terminado; útil para comparación relativa.
- Resource Utilization Efficiency: eficiencia de GPUs y TPUs en training e inferencia; detecta recursos subutilizados o sobreaprovisionados.
- Training Cost Efficiency: costo total de entrenar un modelo dividido por sus métricas de desempeño.
- Anomaly Detection Rate: frecuencia e impacto de anomalías en el gasto de IA.
- Value for AI Initiatives: retorno financiero o de valor de iniciativas de IA frente a su costo.
- Time to Achieve Business Value: tiempo hasta lograr valor medible, con punto de equilibrio frente a hacer la función por otros medios.
- Time to First Prompt: tiempo de calendario de ingeniería para dejar un servicio listo para su primer uso o pasar de POC a producción.
- Valores numéricos de referencia (metas) para estos KPIs: No publicado en la fuente.

Otras métricas citadas en los papers: costo por caso de uso, desglose de tokens (input/output, cached/uncached, por modelo), utilización de GPU, tasas de error y reintentos; "token use budgeted" por proyecto.

Datos de State of FinOps 2026 sobre IA (https://data.finops.org/): 98% de los equipos gestiona gasto de IA (63% en 2025; 31% en 2024); FinOps for AI es la prioridad futura número uno (33%); AI for FinOps 24%; el principal skillset a incorporar es la gestión de costos de IA; el pedido de herramienta número uno es el monitoreo granular del gasto de IA (tokens, solicitudes LLM, utilización de GPU). Desafíos citados: visibilidad de costos de IA, asignación a unidades de negocio y determinar valor/ROI.

## 11. Recomendaciones por madurez (Crawl, Walk, Run)

Compilación de lo que dicen las fuentes (no existe una tabla oficial única):

| Madurez | Recomendación de las fuentes |
|---|---|
| Crawl | AI for FinOps: modos Inform & explain (responder preguntas, resumir, redactar); bajo riesgo y alto valor explicativo. FinOps for AI: ownership claro, etiquetado de recursos de IA, visibilidad básica de costos, revisión frecuente de proyectos, umbrales a nivel empresa. |
| Walk | AI for FinOps: introducir Analyze & detect y Recommend con validación humana manual. FinOps for AI: umbrales por proyecto, funding incremental, cost per use case, AI gateway con registro de metadatos, AI Investment Council. |
| Run | AI for FinOps: casos agentic y Act & automate viables, con circuit breakers, límites de iteración y revisión humana antes de ejecutar; shift-left en CI/CD. FinOps for AI: Unit Economics por salida de negocio, clasificación de cargas con Big-T, gobierno de agentes, ciclo de vida y exit criteria de herramientas. |

Advertencia de la fuente: adoptar enfoques autónomos sin tagging, atribución y gobernanza robustos produce resultados poco confiables.
