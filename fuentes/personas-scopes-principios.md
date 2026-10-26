# FinOps Framework - Personas, Scopes, Principles, Domains y Phases

Fuentes (todas FinOps Foundation, CC BY 4.0, leídas el 2026-10-26):
- https://www.finops.org/framework/personas/
- https://www.finops.org/framework/scopes/
- https://www.finops.org/framework/principles/
- https://www.finops.org/framework/domains/
- https://www.finops.org/framework/phases/

Resumen en español de Chile; nombres oficiales en inglés.

---

## 1. Personas

Implementar FinOps requiere muchos stakeholders (Personas) que colaboren con el equipo FinOps; no solo el equipo FinOps ejecuta actividades FinOps. Las Personas son grupos amplios de stakeholders, no individuos: en una organización compleja una Persona abarca varios roles o cargos, y en una muy pequeña una sola persona puede cumplir varias Personas. Cada una tiene perspectivas, desafíos, métricas y resultados distintos.

### Core Personas

| Persona | Rol (definición de la fuente) | Responsabilidades FinOps listadas |
|---|---|---|
| FinOps Practitioner | Puente entre equipos de negocio, ingeniería y finanzas; aplica conocimiento del FinOps Framework para establecer una cultura FinOps y habilitar decisiones basadas en evidencia que maximicen el valor de negocio de la nube. | Broad Technical Proficiency; Analytical Skills; Cost Management and Optimization; Collaboration and Communication; FinOps Practice Continuous Improvement; Problem-Solving; Change Management; FinOps Team Leadership and Centralized FinOps Functions |
| Engineering | Diseña, construye, gestiona y optimiza la infraestructura tecnológica para lograr costo-efectividad, desempeño, confiabilidad, seguridad y cumplimiento en todas las technology categories. | Architecture and Design; Cloud Infrastructure and Platform Management; Application and Services Development and Deployment; Cost Management and Resource Optimization; Monitoring and Alerting; Security and Compliance; Automation and Tooling Implementation; Sustainability Considerations |
| Finance | Aporta experticia financiera y trabaja con FinOps Practitioners para cuantificar el valor de negocio del gasto tecnológico, apoyar forecasts, presupuesto y chargeback, y definir el contexto financiero y contable de las decisiones informadas por FinOps (en contexto de IT Financial Management y a nivel organizacional). | Financial Expertise and Organizational Finance Policy; Budgeting and Forecasting Support; Cost Allocation Analysis; Financial Reporting; Compliance and Governance; Invoice Reconciliation and Accounting Compliance |
| Product | Genera valor de negocio definiendo requisitos de producto, priorizando iniciativas que alinean FinOps con objetivos de negocio e inversiones estratégicas, involucrando stakeholders y articulando la propuesta de valor de las decisiones tecnológicas. | Strategic Product and Portfolio Alignment; Stakeholder Engagement; Requirement Definition; Value Delivery; Change Management |
| Procurement | Adquiere tecnología en todas las categorías, optimiza y mejora relaciones con proveedores, asegura contratos costo-efectivos y conformes; colabora con FinOps Practitioners para que las decisiones que afectan el valor de las compras se tomen con la cadencia adecuada. | Vendor Risk Management; Vendor Contract Management and Negotiation; Strategic Vendor Relationship Management; Vendor Selection Support; Vendor Negotiation and Discount Management; Collaboration with IT and Operations; License Monitoring and Evaluation; Compliance and Governance |
| Leadership | Fija y promueve los objetivos de negocio y técnicos, habilita la alineación organizacional para priorizar iniciativas FinOps e impulsa la acción para lograr una cultura de rendición de cuentas y decisiones habilitadas por FinOps. | Strategic Business and Technology Objective Setting; Decision-Making and Prioritization Authority; Stakeholder Engagement and Alignment; Revenue Growth or other Organizational Success Criteria Owner; Compliance and Governance |

### Allied Personas
Roles no directamente involucrados en la práctica de FinOps pero que pueden requerir coordinación con FinOps Practitioners. Trabajan en disciplinas tradicionales o emergentes: Sustainability, ITAM, ITFM/TBM, Security e ITSM/ITIL. Se alinean con la Capability "Intersecting Disciplines".

Sobre qué espera cada Persona de FinOps (métricas o expectativas específicas por Persona): la página lista el rol y las responsabilidades, pero no un detalle adicional de expectativas. Detalle adicional: "No publicado en la fuente".

---

## 2. Principles

Actúan como "north star" de la práctica. Sin orden particular; todos son importantes. Texto de los puntos de apoyo tomado de la fuente.

### 2.1 Teams need to collaborate
- Finance, technology, product y leaders trabajan juntos para gestionar cada technology category a la velocidad y granularidad que requiere.
- La coordinación desde ejecutivos hasta ingenieros, y entre todas las Personas, asegura foco en los objetivos estratégicos más valiosos.
- Los equipos trabajan juntos para mejorar continuamente en eficiencia e innovación.

### 2.2 Business value drives technology decisions
- Las unit economic y las métricas basadas en valor demuestran mejor el impacto de negocio que el gasto agregado o categorizado.
- Tomar decisiones conscientes de trade-off entre costo, calidad y velocidad.
- Usar las fortalezas de cada technology category para derivar valor y apoyar la innovación.
- Diferenciar con FinOps Scopes para apuntar al valor de negocio de objetivos organizacionales específicos.

### 2.3 Everyone takes ownership for their technology usage
- La responsabilidad por uso y costo se traslada al borde, con ingenieros asumiendo costos desde el diseño de arquitectura hasta la operación.
- Equipos de feature y producto pueden gestionar su mezcla de uso contra presupuestos que ayudan a controlar.
- Descentralizar las decisiones sobre arquitectura costo-efectiva, uso de recursos y optimización.
- Los equipos técnicos deben considerar el costo como métrica de primera clase desde el inicio del ciclo de desarrollo de software.

### 2.4 FinOps data should be accessible, timely, and accurate
- Procesar y compartir datos de costo apenas estén disponibles.
- La visibilidad en tiempo real impulsa de forma autónoma un mejor uso de la tecnología; los ciclos de feedback rápidos generan conducta más eficiente.
- Visibilidad consistente del gasto tecnológico a todos los niveles de la organización.
- Crear, monitorear y mejorar el forecasting y la planificación financiera en tiempo real.
- El análisis de tendencias y varianza ayuda a explicar los costos.
- El benchmarking interno entre equipos impulsa mejores prácticas y celebra logros.
- Usar FOCUS y otros métodos para mejorar continuamente normalización, exactitud y consistencia de datos entre technology categories.

### 2.5 FinOps should be enabled centrally
- Una función FinOps centralizada fomenta, evangeliza y habilita mejores prácticas en un modelo de responsabilidad compartida.
- La comunicación ejecutiva y la alineación con estrategias de negocio y tecnología se habilitan mejor con un equipo o función central.
- La optimización de rates, commitments y descuentos se centraliza mejor para aprovechar economías de escala y dejar a Engineering enfocado en optimizar su uso.

### 2.6 Take advantage of the variable cost model of the cloud
- Cada technology category (public cloud, data center, SaaS, Licenses, Data Cloud Platforms, etc.) implica modelos de costo con pros y contras.
- Una proporción creciente de cada categoría es basada en consumo, granular y más variable; aplicar lo aprendido en cloud a otras categorías.
- El modelo variable de la nube, el fijo del data center u otros ofrecen oportunidades de entregar más valor; decidir no solo por requisitos técnicos sino por consideraciones de modelo de costo.
- Adoptar predicción, planificación y compra de capacidad just-in-time donde sea valioso para reducir desperdicio.
- La planificación ágil iterativa se prefiere a la planificación estática de largo plazo en una proporción creciente del parque tecnológico.
- Pasar a un diseño de arquitectura más proactivo con ajustes continuos, en vez de limpiezas reactivas poco frecuentes.

---

## 3. Scopes

Definición: un FinOps Scope es un segmento definido de gasto a través de technology categories, alineado a constructos de negocio (producto, centro de costo, ambiente), que guía la aplicación de FinOps para maximizar el valor tecnológico.

- Establecen el contexto de decisión y una referencia compartida para alinear stakeholders, actividades y resultados. Permiten desarrollar perfiles de práctica que determinan qué Personas participan, qué Capabilities se aplican y qué Domains definen el éxito.
- Una práctica suele definir varios Scopes. Consideraciones: frecuencia con que se realiza cada Capability, rigor de la gobernanza, nivel esperado de KPIs, amplitud de la optimización. Incluir o excluir un elemento del Framework en un Scope debe ser intencional.
- La meta de una Capability (ej. Data Ingestion, Allocation, Forecasting) es consistente, pero sus insumos, KPIs, madurez y medidas de éxito varían por Scope según las decisiones que apoya.
- Ejemplo de la fuente: un despliegue Kubernetes híbrido entre nube pública y data center on-premises puede ser un Scope propio.

### Qué impulsa los Scopes (tres ideas de la fuente)
1. Dirigidos por la estrategia de negocio y tecnología: las Capabilities se adaptan y priorizan por Scope; las Personas se involucran o excluyen según la rendición de cuentas requerida.
2. Reflejan contexto de decisión, no límites de infraestructura: un Scope puede abarcar varios productos, centros de costo o ambientes; pueden existir varios Scopes sobre un mismo gasto si hay objetivos distintos.
3. Determinan cómo se involucran Personas, Domains y Capabilities, según madurez, prioridades y velocidad de innovación deseada.

Regla de creación: crear un Scope nuevo solo cuando habilita mejores decisiones; mantenerlos pocos, simples y con propósito.

### Evolución
- Muchas prácticas parten con un Scope por defecto alineado al uso de cloud ("Cloud FinOps"), que en realidad refleja objetivos de negocio (eficiencia de costo, modernización, velocidad de entrega).
- Luego surgen Scopes específicos por contexto de negocio. Ejemplos de la fuente: valor de un portafolio de productos clave; gasto en una iniciativa de innovación; una aplicación nueva para expandirse a un mercado; gasto asociado a lograr cumplimiento SOC2 o FedRAMP.
- Con el tiempo los Scopes abarcan categorías más allá de la nube pública. En áreas como IA, el Scope se define menos por dónde corre la tecnología y más por en qué invierte el negocio, cómo apoya diferenciación o innovación y cómo se mide el éxito.

### De preguntas de negocio a Scopes (técnica Five whys)
Los Scopes se inician por expectativas explícitas del negocio, normalmente preguntas de Leadership. Ejemplo de la fuente: "What are we spending on AI?" Con Five whys se llega a: entender cómo usan IA Team A y Team B, invertir en la infraestructura de IA adecuada para los equipos de producto clave, impulsar innovación para diferenciarse, mantenerse por delante de competidores y crecer cuota de mercado. Solo con ese contexto se define el Scope, moldeado por el objetivo de negocio y no por la tecnología.

### Ciclo de vida e interacción
- Los Scopes son situacionales: varían en duración e intensidad; al cumplirse o perder relevancia el resultado, la práctica se adapta o deja que las actividades se extingan.
- No son mutuamente excluyentes: un uso tecnológico puede estar en varios Scopes. Ejemplo de la fuente: Scope de gasto cloud total con forecasting muy preciso y mínima varianza, y otro Scope de gasto en Agentic AI para productividad de desarrolladores con mayor tolerancia a experimentación y variabilidad. El equipo debe decidir si excluye la IA del Scope cloud o la mantiene contabilizando explícitamente su contribución a la varianza del forecast.

Activos relacionados listados en la página: FinOps for AI Overview; Model Context Protocol (MCP): An AI for FinOps Use Case; Driving Cost Efficiency into AI Deep Learning Pipelines with FinOps; Introduction to FinOps for SaaS; Applying the FinOps Framework to SaaS at Scale; How FinOps Tools and Practices Can Help Control Licensing and Other Costs (Expedia Group); Effect of Optimization on AI Forecasting; FinOps Considerations for a Data Center; Context for Building a FinOps Practice for Data Cloud Platforms.

---

## 4. Domains

"Los Domains son los resultados de una práctica FinOps": describen los resultados de negocio fundamentales que se deben lograr. Cada Domain agrupa Capabilities; las organizaciones desarrollan las que les aportan valor según su necesidad y madurez. No todas las organizaciones invertirán en toda Capability, pero toda organización que usa cloud (más Scopes adicionales) realizará actividades en cada Domain.

| Domain | Resultado | Capabilities |
|---|---|---|
| Understand Usage & Cost | Mejor comprensión del uso de tecnología: reunir información (costos y uso directos e imputados, compromisos contractuales, observabilidad, utilización, datos de sostenibilidad, datasets de contexto); definir metadata organizacional para categorizar, asignar y resumir costo y uso; definir reportería y analítica disponible para todas las Personas. | Data Ingestion; Allocation; Reporting & Analytics; Anomaly Management |
| Quantify Business Value | Conectar datos de uso y costo con el valor de negocio que crean, de modo que el valor sea transparente y esté dentro de lo esperado: mapear costos monetarios y no monetarios a presupuestos, forecast con historia y planes futuros, KPIs técnicos y organizacionales, benchmarking entre equipos, unidades de negocio y otras organizaciones. | Planning & Estimating; Forecasting; Budgeting; KPIs & Benchmarking; Unit Economics |
| Optimize Usage & Cost | Usar recursos solo cuando aportan valor y comprarlos al menor costo e impacto aceptable. La eficiencia se mide en costo monetario, carbono o medidas operativas de TI. Incluye modernización de arquitectura, sostenibilidad y SaaS licenciado o por consumo. | Architecting & Workload Placement; Rate Optimization; Usage Optimization; Sustainability; Licensing & SaaS |
| Manage the FinOps Practice | Mejora continua para alinear personas, procesos y tecnología y adoptar FinOps aplicando el Framework a sus Scopes; operación efectiva, habilitación de toda la organización e interacción con otras Personas y funciones. | FinOps Practice Operations; Governance, Policy & Risk; FinOps Assessment; Automation, Tools, & Services; FinOps Education & Enablement; Invoicing & Chargeback; Intersecting Disciplines; Executive Strategy Alignment |

Notas de la fuente: los Domains no son pasos de un proceso serial (se trabajan en paralelo); todos los Domains y Capabilities son interdependientes; los tres primeros describen las prácticas para el uso exitoso de cloud y el cuarto las actividades para que la propia práctica FinOps sea exitosa.

---

## 5. Phases (lifecycle Inform, Optimize, Operate)

FinOps se realiza trabajando iterativamente las Capabilities en tres Phases. Los practitioners ciclan rápidamente entre ellas; distintos miembros del equipo pueden trabajar fases distintas o con distinta cadencia. La acción rápida y regular evita la parálisis por análisis y refuerza empezar pequeño y crecer.

### Inform - Visibility & Allocation
- Examinar datos de costo, uso y eficiencia. Actividades en Data Ingestion, Allocation, Reporting & Analytics, Forecasting y Unit Economics permiten evaluar presupuesto, tendencias de forecast, KPIs, benchmark y métricas que revelan el valor de negocio del estado tecnológico actual.
- La asignación precisa del gasto y uso entre cualquier technology category habilita reportería precisa; evitar sorpresas, pronosticar gasto y costos de carbono.
- La naturaleza on-demand y elástica de cloud, SaaS e IA, con precios y descuentos complejos, exige revisitar Inform continuamente para validar el impacto de las optimizaciones.

### Optimize - Rates & Usage
- Identificar oportunidades de mejorar eficiencia y valor con la vista reunida en Inform. Cada technology category tiene opciones distintas: en cloud, rightsizing de recursos subutilizados, arquitecturas modernas, gestión de workloads, eliminación automatizada de desperdicio; en SaaS y licencias, cambios de contrato, racionalización de proveedores, retiro de licencias sin uso.
- Usage optimization (usar menos recursos para un resultado aceptable) requiere colaborar principalmente con Engineering; rate optimization (pagar un monto apropiado por lo que se debe usar) con Procurement y Leadership.
- Las opciones pueden competir: usar un proceso colaborativo y criterios definidos para priorizar y mantener un backlog.

### Operate - Continuous Improvement & Usage
- Implementar los cambios identificados en Optimize. Incluso acciones pequeñas e incrementales impactan las unit metrics y el valor producido.
- Requiere cultura de rendición de cuentas entre ingeniería, finanzas y negocio. Algunas acciones consisten en madurar Capabilities o evolucionar las operaciones FinOps, no solo ajustes de uso o tarifas.
- Se vuelve continuamente a Inform y Optimize.
