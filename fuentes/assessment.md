# FinOps Assessment Guide - metodología oficial

Fuente: https://www.finops.org/wg/finops-assessment/ (FinOps Foundation, licencia CC BY 4.0, última actualización publicada: February 18, 2026). Resumen en español de Chile; términos oficiales en inglés y criterios de lentes citados de forma fiel.

## Propósito y alcance

- FinOps no es un proceso lineal con inicio y fin, sino una práctica continua que debe madurar según cambia el entorno tecnológico (Cloud, SaaS, PaaS, Data Centers, Data Cloud Platforms).
- La guía se usa junto con el FinOps Framework para entender la madurez operativa actual y las áreas de atención.
- Puede aplicarse a cualquier nivel: equipos de servicio o funcionales, divisiones, unidades de negocio u organización completa.
- Objetivo declarado: no es un análisis de precisión que "califique" la práctica, sino una visión general de alto nivel para identificar áreas puntuales a investigar o desarrollar.
- No es necesario evaluar todas las Capabilities a la vez; se puede apuntar a una Capability o a un conjunto relacionado dentro de un Domain.
- En cada evaluación se debe definir con claridad el Target Scope (qué Capabilities) y el Target Group (qué parte de la organización). Incluir a quienes tienen impacto primario y, opcionalmente, a futuros objetivos para que ganen experiencia.

## Términos clave

| Término | Definición de la fuente |
|---|---|
| Lens(es) | Vistas funcionales de inspección para analizar cualquier Capability; cada una requiere distinto esfuerzo y evidencia. |
| Domain | Esfera de actividad o conocimiento diseñada para lograr un resultado para la organización. |
| Capability | Área funcional de actividad en apoyo de su Domain; incluye definiciones, personas clave, métricas de desempeño y actividades. |
| Framework | Vista estructural de extremo a extremo del modelo de entrega de una práctica FinOps (Domains, Capabilities, lifecycle, maturity model, principios). |
| Maturity | Medida aplicada de forma consistente de experiencia, amplitud de capacidad y éxito en la entrega de un elemento del Framework. No es algo a alcanzar por sí mismo, sino que se desarrolla ante la necesidad de manejar más complejidad cuando produce valor. |
| Discovery | Preguntas preámbulo que forman la base para entender el nivel de madurez que se fijará. |
| Target Score | Meta pretendida para una práctica. Ejemplo de la fuente: con máximo de 20 por Capability (5 lenses x máximo 4), un 12 de 20 puede ser "suficiente" para la hoja de ruta actual, sobre todo en una Capability nueva. |

## Los cinco Lenses (escala 0 a 4)

Cada lens tiene cinco niveles descriptivos. No se necesita operar en niveles altos en todos los casos; leer el nivel siguiente ayuda a decidir si aporta valor. Aplicar los lenses de forma consistente es crítico para comparar en el tiempo.

### Lens 1: Knowledge
Amplitud de comprensión y conocimiento de la Capability en el Target Group (qué tan clara es la comunicación, qué tan conocidos son conceptos, términos y procesos).

| Nivel | Heading | Descripción |
|---|---|---|
| 0 | No Knowledge | Conocimiento efectivamente inexistente en el Target Group; no hay discusiones ni nadie desarrollándolo. |
| 1 | Partial Knowledge | Conocimiento preliminar empieza a difundirse entre stakeholders clave, pero aún no es común en el grupo. |
| 2 | Developing Knowledge | Conocimiento básico entendido por un número limitado de stakeholders clave; información limitada en difusiones no escaladas. |
| 3 | Full Knowledge | Conocimiento sólido en todo el grupo, con onboarding inicial y refuerzo periódico por capacitación u otros medios. |
| 4 | Knowledge Leader | El grupo impulsa la conciencia hacia otros grupos pares y la industria; mejora y genera nuevas perspectivas. |

### Lens 2: Process
Acciones para entregar la Capability y artefactos que las definen y documentan; eficacia, validez y prevalencia.

| Nivel | Heading | Descripción |
|---|---|---|
| 0 | No Process | Sin procesos descritos y consistentes que gobiernen algún aspecto. |
| 1 | Implementing Process | Procesos en formación, definición y posiblemente prueba; aún no formalizados como BAU. |
| 2 | Developing POC Process | Procesos funcionales, acordados y seguidos al menos por algunos equipos. |
| 3 | Scaled Process | Procesos escalados, documentados, con ciclos de retroalimentación periódicos. |
| 4 | Mature (Agile) Process | Procesos claros, transparentes, totalmente integrados y consistentes; iterados con feedback de stakeholders y refinamiento ágil continuo (no implica un único proceso por tarea). |

### Lens 3: Metrics
¿Se mide la Capability? ¿Hay forma de probar progreso en el tiempo? Este lens no mide qué tan altos son los valores de las métricas, sino cómo se definen y usan las mediciones.

| Nivel | Heading | Descripción |
|---|---|---|
| 0 | No Metrics | Sin mediciones; sin visibilidad del estado o progreso. |
| 1 | Identified Metrics | Métricas clave identificadas que el negocio considera valiosas para decisiones de trade-off. |
| 2 | Baselined Metrics | Métricas iniciales generadas manualmente, con medición tipo semáforo (Red/Yellow/Green). |
| 3 | Established & collecting Metric Targets data | KPIs vigentes para al menos parte de la Capability en el grupo y cadencia de recolección establecida. |
| 4 | Mature, Global KPIs | KPIs S.M.A.R.T. globales, automatizados e iterados con cadencia regular; ligados directamente a metas y desempeño del negocio. |

### Lens 4: Adoption
Qué tan ampliamente el Target Group adoptó y aceptó la Capability (con su conocimiento, procesos y métricas) como parte integral de sus funciones.

| Nivel | Heading | Descripción |
|---|---|---|
| 0 | No Adoption | La Capability no existe en ningún lugar del grupo. |
| 1 | Siloed Adoption | Elementos adoptados por un grupo aislado, sin estandarización ni evidencia de mejores prácticas. |
| 2 | Initial Standardized Adoption | Elementos tempranos estandarizados y validados por pocas personas. |
| 3 | Key Adoption | Elementos estandarizados plenamente establecidos como parte del BAU de la mayoría del grupo. |
| 4 | Full Adoption | La Capability existe en la totalidad de los elementos del grupo y se trabaja activamente. |

### Lens 5: Automation
Automatizar tareas repetibles con puntos de decisión predecibles da consistencia, velocidad y escalabilidad.

| Nivel | Heading | Descripción |
|---|---|---|
| 0 | No Automation | Prácticamente todas las acciones son manuales. |
| 1 | Identified Automation Opportunities | Se identifican y mapean requisitos de automatización para reducir trabajo y toil. |
| 2 | Experimental Automation | Adopción temprana: algunas acciones clave se optimizan con flujos o soluciones automatizadas. |
| 3 | Primary Automation | Las acciones principales o más demandantes ya fueron delegadas a automatización. |
| 4 | Full Automation | Todas las tareas materiales y repetibles están automatizadas; las nuevas se revisan por potencial de automatización. |

## Etapas del proceso

### Stage 1: Introduction (definir parámetros)
Parámetros a definir: Target Group, Target Scope, Lens Weighting, Target Score.

- Target Group: enfocarse en grupos que destaquen; mejor uno o pocos grupos que promedios entre grupos de madurez muy distinta. Atributos de ejemplo: agrupación de asignación de costos cloud, equipo(s) de ingeniería, producto/servicio, proyecto/iniciativa, Business Owner.
- Para repetir evaluaciones (tendencias y baseline) se debe usar el mismo Target Scope y Target Group, y conservar registro del alcance y de cada baseline y análisis.
- Target Scope: analizar todas las Capabilities (22 al momento de la fuente) es excesivo. Elegir las de mayor valor de negocio. Para quien parte, suele ser el Domain Understand Cloud Usage & Cost; para más establecidos, Optimize Cloud Usage & Cost, Quantify Cloud Value o Manage the FinOps Practice.
- Ejemplo de la fuente para organización que recién adopta FinOps: Allocation, Reporting & Analytics, Data Ingestion (sobre todo sin herramienta de terceros), Rate Optimization, Workload Optimization y FinOps Education & Enablement. Para una más avanzada: Forecasting, Budgeting, Invoicing & Chargeback y Unit Economics.
- Lens Weighting: ponderar los cinco lenses según lo realista y lo importante. Ejemplo: si hay poco conocimiento y proceso, ponderar más esos y reducir el peso de Automation.
- Target Scores: fijar metas realistas de corto plazo por Capability; algunas ameritan nivel alto, otras son disciplinas nuevas.
- Stakeholders y SMEs: se derivan del Target Scope y Target Group; distintas Capabilities requieren distintos stakeholders y personas adyacentes. Registrar sus datos y aportes de evidencia; considerarlos al fijar Target Scores.

### Stage 2: Measure (cuestionario y puntaje)
- Planificar conversaciones; agrupar Capabilities que comparten SMEs.
- Capability Overview: breve resumen del Target Scope para que todos conozcan qué es cada Capability y dónde encaja; confirmar alcance y aprovechar para educar.
- Gathering Evidence: antes de los cinco lenses, hacer Discovery Questions. Se recomienda curar una biblioteca de preguntas de descubrimiento por Capability. Reunir evidencia documental y asociarla a la evaluación. La página no publica el listado de preguntas (el cuestionario concreto no está en la página): "No publicado en la fuente".
- Conducting the Assessment: para cada lens, decidir un puntaje de madurez con la evidencia y el contexto, de forma consistente y justa.
- Desacuerdo entre entrevistados: se considera positivo; revela falta de entendimiento o experiencia común y una oportunidad de educar, habilitar y alinear.
- Escala de puntaje: cada Capability se puntúa como porcentaje del máximo posible. Con escala 0 a 4 y 5 lenses, máximo 20 por Capability. Cada lens puede ponderarse según prioridades. Si se evalúan varias Capabilities se puede agregar para un resultado global y destacar áreas con puntaje bajo o cero.

### Stage 3: Outcome (interpretación)
- Desglosar los puntajes en componentes (lenses) por Capability para ver fortalezas, debilidades y esfuerzo asociado.
- Ejemplo de lectura de la fuente: Knowledge y Process fuertes, Adoption creciente, Metrics por mejorar, Automation iniciada solo en algunas Capabilities. Una Capability con buen puntaje (ej. Reporting & Analytics) sirve de base para otras dependientes (ej. Anomaly Management).
- Con los datos se identifican áreas de mejora, bloqueadores y se arma una hoja de ruta para lograr un delta en la siguiente evaluación.
- Reevaluación: conservar los datos y repetir periódicamente con el mismo alcance y criterios permite resaltar cambios de puntaje en la grilla y mostrar tendencia. Frecuencia numérica de reevaluación: "No publicado en la fuente".

### Stage 4: Focus (priorización de brechas)
- Usar los datos para profundizar en un área con las Discovery Questions.
- Ejemplo de la fuente: Managing Shared Cost (hoy parte de Allocation en Framework 2024) con puntaje cero en Metrics y Automation: no hay forma de saber su efectividad y el éxito depende del esfuerzo humano, lo que puede ser un riesgo; agregar métricas y automatización aumentaría efectividad y liberaría tiempo.
- Triage & Prioritization: considerar la jerarquía de Capabilities (cuáles se usarán intensamente en la siguiente etapa de la hoja de ruta), el análisis del Stage 3 y el contexto del Capability Discovery para fijar la próxima prioridad de aceleración de adopción.

## Entregables y recursos

- Resultado: puntajes por lens y Capability, agregado global, hallazgos de brechas, hoja de ruta/delta para la próxima evaluación, registro de alcance, stakeholders y evidencia.
- Herramienta asociada: "FinOps Assessment Spreadsheet" (enlazada en la página; contenido no leído aquí).
- Working Group reconocido en la fuente: Kim Wier (Target), Vijaya Karthvaya Kudithipudi (Nokia), Rob Wainwright (Rackspace Technology), Mark Butcher (Posetiv Cloud), Ben de Mora (Apptio), Rob Martin y Vasilio Markanastasakis (FinOps Foundation), Ashley Hromatko.
