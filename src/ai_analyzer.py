"""Analizador de historias de usuario usando IA."""

from typing import Dict, Any
import os
from litellm import completion


class AIAnalyzer:
    """Analizador de requerimientos usando modelos de IA."""

    def __init__(self, model: str = "gpt-4", language: str = "en"):
        """
        Inicializa el analizador.
        
        Args:
            model: Modelo de IA a usar (ej: gpt-4, claude-3-opus-20240229)
            language: Idioma para el prompt (es, en)
        """
        self.model = model
        self.language = language
        
        # Configurar las API keys desde variables de entorno
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
        os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY", "")

    def create_analysis_prompt(self, story_data: Dict[str, Any]) -> str:
        """
        Crea un prompt estructurado para analizar la historia.
        
        Args:
            story_data: Datos de la historia de usuario
            
        Returns:
            Prompt formateado
        """
        if self.language == "es":
            return self._create_spanish_prompt(story_data)
        else:
            return self._create_english_prompt(story_data)
    
    def _create_english_prompt(self, story_data: Dict[str, Any]) -> str:
        """
        Creates English prompt with advanced prompt engineering techniques:
        - XML-structured prompting for better parsing
        - Chain-of-thought reasoning (5 explicit steps)
        - Context-aware prompting with dynamic analysis
        - Few-shot learning with quality examples
        - Anti-hallucination guidelines
        """
        # Parse story components
        story_context = self._parse_story_context(story_data)
        
        # Build context-aware instructions
        context_notes = self._build_context_notes(story_context, "en")
        
        prompt = f"""<task>
Analyze the following Jira user story to identify gaps, ambiguities, and improvement opportunities.
</task>

<input_data>
<story_metadata>
ID: {story_data['key']}
Title: {story_data['title']}
Status: {story_data['status']}
Priority: {story_data['priority']}
Labels: {', '.join(story_data['labels']) if story_data['labels'] else 'None'}
</story_metadata>

<story_description>
{story_data['description'] or 'No description provided'}

{f"\\n--- ADDITIONAL CONTEXT FROM ANALYST ---\\n{story_data['user_notes']}\\n--- END OF ADDITIONAL CONTEXT ---" if story_data.get('user_notes') else ''}
</story_description>

<acceptance_criteria>
{story_data['acceptance_criteria'] or 'No acceptance criteria specified'}
</acceptance_criteria>

<additional_context>
{self._format_comments(story_data['comments'])}
</additional_context>

<context_analysis>
{context_notes}
</context_analysis>
</input_data>

<analysis_methodology>
Follow this chain-of-thought approach:

1. UNDERSTAND: First, identify the core user need
   - Who is the user?
   - What do they want to accomplish?
   - Why is this valuable?
   - Consider any additional context or notes provided by the user

2. DECOMPOSE: Break down the requirement
   - What are the main components?
   - What are the dependencies?
   - What are the success criteria?

3. IDENTIFY GAPS: Look for missing information
   - What assumptions are implicit?
   - What edge cases exist?
   - What could go wrong?
   - What questions arise from the user's notes?

4. ASSESS QUALITY: Evaluate completeness
   - Are criteria SMART and testable?
   - Are non-functional requirements addressed?
   - Is the scope clear?
   - Do the user notes highlight specific concerns?

5. FORMULATE QUESTIONS: What needs clarification?
   - Business logic questions
   - Technical implementation questions
   - Testing and validation questions
   - Questions related to user-provided context
</analysis_methodology>

<output_format>
Provide your analysis using this exact structure:

## 1. REQUIREMENT SUMMARY

User Story: As a [who], I want [what], so that [why]
Business Value: [One sentence describing business impact]
Core Functionality: [2-3 sentences describing main feature]

## 2. KEY REQUIREMENTS (What needs to be built)

**Core Features:**
- [Feature 1: Clear description]
- [Feature 2: Clear description]
- [Feature 3: Clear description]

**User Interactions:**
- [How users will interact with this feature]

**Expected Outcomes:**
- [What should happen when feature works correctly]

## 3. REQUIREMENT STRUCTURE

**Actors:** [Comma-separated list]

**Main Flow:**
1. [Step 1]
2. [Step 2]
...

## 4. ACCEPTANCE CRITERIA (Restructured)

Organize and clarify the acceptance criteria in Given-When-Then format:

**Scenario 1: [Name]**
- Given: [Precondition]
- When: [Action]
- Then: [Expected result]

**Scenario 2: [Name]**
- Given: [Precondition]
- When: [Action]
- Then: [Expected result]

[Add more scenarios as needed based on the story]

## 5. MISSING INFORMATION

**Critical Gaps (Must clarify before development):**
- [Item 1]
- [Item 2]

**Non-Functional Requirements:**
- Performance: [What's missing or "Not specified"]
- Security: [What's missing or "Not specified"]
- Scalability: [What's missing or "Not specified"]

**Edge Cases to Consider:**
- [Case 1: Description]
- [Case 2: Description]

## 6. CLARIFICATION QUESTIONS

**For Product Owner:**
1. [Specific question about business logic]
2. [Specific question about user experience]
3. [Specific question about priorities]

**For Technical Team:**
1. [Specific question about implementation]
2. [Specific question about integration]
3. [Specific question about constraints]

**For QA/Testing:**
1. [Specific question about test scenarios]
2. [Specific question about error handling]
3. [Specific question about validation]

## 7. RECOMMENDATIONS

**To Improve Clarity:**
- [Suggestion 1 to make requirements clearer]
- [Suggestion 2 to make requirements clearer]

**To Ensure Completeness:**
- [What should be added to make story complete]

**Risk Mitigation:**
- [Risk 1]: [Mitigation strategy]
- [Risk 2]: [Mitigation strategy]
</output_format>

<guidelines>
- Be specific and actionable in all recommendations
- FOCUS ON WHAT'S PRESENT: Start by clearly identifying and organizing what information IS provided
- Restructure information to make it clearer and more actionable
- Highlight key requirements and core functionality
- Provide concrete examples when identifying problems
- Use bullet points for lists, numbered lists for sequences
- Limit each section to the most important 3-5 items

CRITICAL ANTI-HALLUCINATION RULES:
- Base your analysis EXCLUSIVELY on information explicitly provided in the story description, acceptance criteria, comments, and analyst notes above
- DO NOT invent, assume, or hallucinate features, requirements, technical details, or functionality not explicitly mentioned
- When referencing functionality, use ONLY the exact terms, phrases, and language from the story itself
- DO NOT add technical implementation details unless they are explicitly stated in the story
- DO NOT assume technologies, frameworks, databases, or tools unless explicitly mentioned
- If you need to suggest something new, clearly mark it as "RECOMMENDATION" or "SUGGESTION", not as existing functionality
- When in doubt about whether something was mentioned, DO NOT include it - only reference what is explicitly stated
- If the story lacks information, point out what's missing rather than filling in the gaps with assumptions

CONSTRUCTIVE APPROACH:
- Start with what's clear and well-defined
- Reorganize information to make it more structured
- Extract key points and make them prominent
- Then identify gaps in a helpful, constructive manner
- Provide recommendations to improve, not just criticize
</guidelines>

<example_quality>
Good: "The error handling for invalid user input is not specified. What should happen if the user enters a negative quantity?"
Bad: "Error handling needs work."

Good: "Performance requirement missing: What is the acceptable response time for search queries with 10,000+ results?"
Bad: "Performance not mentioned."
</example_quality>"""

        return prompt
    
    def _create_spanish_prompt(self, story_data: Dict[str, Any]) -> str:
        """
        Crea el prompt en español con técnicas avanzadas de prompt engineering:
        - XML-structured prompting para mejor parsing
        - Chain-of-thought reasoning (5 pasos explícitos)
        - Context-aware prompting con análisis dinámico
        - Few-shot learning con ejemplos de calidad
        - Anti-hallucination guidelines
        """
        # Parse story components
        story_context = self._parse_story_context(story_data)
        
        # Build context-aware instructions
        context_notes = self._build_context_notes(story_context, "es")
        
        prompt = f"""<tarea>
Analiza la siguiente historia de usuario de Jira para identificar brechas, ambigüedades y oportunidades de mejora.
</tarea>

<datos_entrada>
<metadatos_historia>
ID: {story_data['key']}
Título: {story_data['title']}
Estado: {story_data['status']}
Prioridad: {story_data['priority']}
Etiquetas: {', '.join(story_data['labels']) if story_data['labels'] else 'Ninguna'}
</metadatos_historia>

<descripcion_historia>
{story_data['description'] or 'No se proporcionó descripción'}

{f"\\n--- CONTEXTO ADICIONAL DEL ANALISTA ---\\n{story_data['user_notes']}\\n--- FIN DEL CONTEXTO ADICIONAL ---" if story_data.get('user_notes') else ''}
</descripcion_historia>

<criterios_aceptacion>
{story_data['acceptance_criteria'] or 'No se especificaron criterios de aceptación'}
</criterios_aceptacion>

<contexto_adicional>
{self._format_comments(story_data['comments'])}
</contexto_adicional>

<analisis_contexto>
{context_notes}
</analisis_contexto>
</datos_entrada>

<metodologia_analisis>
Sigue este enfoque de razonamiento en cadena:

1. COMPRENDER: Primero, identifica la necesidad central del usuario
   - ¿Quién es el usuario?
   - ¿Qué quiere lograr?
   - ¿Por qué es valioso?
   - Considera cualquier contexto o notas adicionales proporcionadas por el usuario

2. DESCOMPONER: Desglosa el requerimiento
   - ¿Cuáles son los componentes principales?
   - ¿Cuáles son las dependencias?
   - ¿Cuáles son los criterios de éxito?

3. IDENTIFICAR BRECHAS: Busca información faltante
   - ¿Qué suposiciones son implícitas?
   - ¿Qué casos edge existen?
   - ¿Qué podría salir mal?
   - ¿Qué preguntas surgen de las notas del usuario?

4. EVALUAR CALIDAD: Evalúa la completitud
   - ¿Los criterios son SMART y verificables?
   - ¿Se abordan los requisitos no funcionales?
   - ¿El alcance está claro?
   - ¿Las notas del usuario destacan preocupaciones específicas?

5. FORMULAR PREGUNTAS: ¿Qué necesita aclaración?
   - Preguntas de lógica de negocio
   - Preguntas de implementación técnica
   - Preguntas de pruebas y validación
   - Preguntas relacionadas con el contexto proporcionado por el usuario
</metodologia_analisis>

<formato_salida>
Proporciona tu análisis usando esta estructura exacta:

## 1. RESUMEN DEL REQUERIMIENTO

Historia de Usuario: Como [quién], quiero [qué], para [por qué]
Valor de Negocio: [Una oración describiendo el impacto de negocio]
Funcionalidad Principal: [2-3 oraciones describiendo la característica principal]

## 2. REQUERIMIENTOS CLAVE (Qué se necesita construir)

**Características Principales:**
- [Característica 1: Descripción clara]
- [Característica 2: Descripción clara]
- [Característica 3: Descripción clara]

**Interacciones del Usuario:**
- [Cómo los usuarios interactuarán con esta característica]

**Resultados Esperados:**
- [Qué debería suceder cuando la característica funcione correctamente]

## 3. ESTRUCTURA DEL REQUERIMIENTO

**Actores:** [Lista separada por comas]

**Flujo Principal:**
1. [Paso 1]
2. [Paso 2]
...

## 4. CRITERIOS DE ACEPTACIÓN (Reestructurados)

Organiza y clarifica los criterios de aceptación en formato Dado-Cuando-Entonces:

**Escenario 1: [Nombre]**
- Dado: [Precondición]
- Cuando: [Acción]
- Entonces: [Resultado esperado]

**Escenario 2: [Nombre]**
- Dado: [Precondición]
- Cuando: [Acción]
- Entonces: [Resultado esperado]

[Agregar más escenarios según sea necesario basándose en la historia]

## 5. INFORMACIÓN FALTANTE

**Brechas Críticas (Deben aclararse antes del desarrollo):**
- [Elemento 1]
- [Elemento 2]

**Requisitos No Funcionales:**
- Rendimiento: [Qué falta o "No especificado"]
- Seguridad: [Qué falta o "No especificado"]
- Escalabilidad: [Qué falta o "No especificado"]

**Casos Edge a Considerar:**
- [Caso 1: Descripción]
- [Caso 2: Descripción]

## 6. PREGUNTAS DE CLARIFICACIÓN

**Para el Product Owner:**
1. [Pregunta específica sobre lógica de negocio]
2. [Pregunta específica sobre experiencia de usuario]
3. [Pregunta específica sobre prioridades]

**Para el Equipo Técnico:**
1. [Pregunta específica sobre implementación]
2. [Pregunta específica sobre integración]
3. [Pregunta específica sobre restricciones]

**Para QA/Testing:**
1. [Pregunta específica sobre escenarios de prueba]
2. [Pregunta específica sobre manejo de errores]
3. [Pregunta específica sobre validación]

## 7. RECOMENDACIONES

**Para Mejorar la Claridad:**
- [Sugerencia 1 para hacer los requisitos más claros]
- [Sugerencia 2 para hacer los requisitos más claros]

**Para Asegurar Completitud:**
- [Qué debería agregarse para hacer la historia completa]

**Mitigación de Riesgos:**
- [Riesgo 1]: [Estrategia de mitigación]
- [Riesgo 2]: [Estrategia de mitigación]
</formato_salida>

<directrices>
- Sé específico y accionable en todas las recomendaciones
- ENFÓCATE EN LO QUE ESTÁ PRESENTE: Comienza identificando y organizando claramente qué información SÍ se proporciona
- Reestructura la información para hacerla más clara y accionable
- Destaca los requisitos clave y la funcionalidad principal
- Proporciona ejemplos concretos al identificar problemas
- Usa viñetas para listas, listas numeradas para secuencias
- Limita cada sección a los 3-5 elementos más importantes

REGLAS CRÍTICAS ANTI-ALUCINACIÓN:
- Basa tu análisis EXCLUSIVAMENTE en la información explícitamente proporcionada en la descripción del story, criterios de aceptación, comentarios y notas del analista
- NO inventes, asumas o alucines características, requisitos, detalles técnicos o funcionalidad que no estén explícitamente mencionados
- Al referenciar funcionalidad, usa ÚNICAMENTE los términos exactos, frases y lenguaje del story mismo
- NO agregues detalles de implementación técnica a menos que estén explícitamente declarados en el story
- NO asumas tecnologías, frameworks, bases de datos o herramientas a menos que estén explícitamente mencionadas
- Si necesitas sugerir algo nuevo, márcalo claramente como "RECOMENDACIÓN" o "SUGERENCIA", no como funcionalidad existente
- Cuando tengas dudas sobre si algo fue mencionado, NO lo incluyas - solo referencia lo que está explícitamente declarado
- Si el story carece de información, señala lo que falta en lugar de llenar los vacíos con suposiciones

ENFOQUE CONSTRUCTIVO:
- Comienza con lo que está claro y bien definido
- Reorganiza la información para hacerla más estructurada
- Extrae los puntos clave y hazlos prominentes
- Luego identifica brechas de manera útil y constructiva
- Proporciona recomendaciones para mejorar, no solo criticar
</directrices>

<ejemplo_calidad>
Bueno: "El manejo de errores para entrada de usuario inválida no está especificado. ¿Qué debería suceder si el usuario ingresa una cantidad negativa?"
Malo: "El manejo de errores necesita trabajo."

Bueno: "Falta requisito de rendimiento: ¿Cuál es el tiempo de respuesta aceptable para consultas de búsqueda con más de 10,000 resultados?"
Malo: "No se menciona el rendimiento."
</ejemplo_calidad>"""

        return prompt

    def _build_context_notes(self, context: Dict[str, Any], language: str) -> str:
        """Build context-aware notes based on what's present/missing."""
        if language == "en":
            notes = []
            if not context['has_description']:
                notes.append("⚠️ WARNING: No description provided - analysis will be limited")
            if not context['has_acceptance_criteria']:
                notes.append("⚠️ WARNING: No acceptance criteria - this is a critical gap")
            if not context['has_comments']:
                notes.append("ℹ️ NOTE: No additional comments or context available")
            if context['priority_level'] in ['High', 'Critical', 'Highest']:
                notes.append(f"⚡ HIGH PRIORITY: This is a {context['priority_level']} priority item - be extra thorough")
            return "\n".join(notes) if notes else "All expected fields are present"
        else:
            notes = []
            if not context['has_description']:
                notes.append("⚠️ ADVERTENCIA: No se proporcionó descripción - el análisis será limitado")
            if not context['has_acceptance_criteria']:
                notes.append("⚠️ ADVERTENCIA: No hay criterios de aceptación - esta es una brecha crítica")
            if not context['has_comments']:
                notes.append("ℹ️ NOTA: No hay comentarios o contexto adicional disponible")
            if context['priority_level'] in ['High', 'Critical', 'Highest', 'Alta', 'Crítica']:
                notes.append(f"⚡ ALTA PRIORIDAD: Este es un elemento de prioridad {context['priority_level']} - sé extra minucioso")
            return "\n".join(notes) if notes else "Todos los campos esperados están presentes"
    
    def _parse_story_context(self, story_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Parse story data to extract structured context.
        
        Args:
            story_data: Raw story data from Jira
            
        Returns:
            Parsed context dictionary
        """
        context = {
            'has_description': bool(story_data.get('description')),
            'has_acceptance_criteria': bool(story_data.get('acceptance_criteria')),
            'has_comments': bool(story_data.get('comments')),
            'has_labels': bool(story_data.get('labels')),
            'priority_level': story_data.get('priority', 'Unknown'),
            'status': story_data.get('status', 'Unknown')
        }
        return context
    
    def _format_comments(self, comments: list) -> str:
        """Formatea los comentarios para el prompt."""
        if not comments:
            return "No hay comentarios"
        
        formatted = []
        for i, comment in enumerate(comments, 1):
            formatted.append(f"Comentario {i}: {comment}")
        
        return "\n".join(formatted)

    def analyze_story(self, story_data: Dict[str, Any], callback=None) -> str:
        """
        Analiza una historia de usuario usando IA con streaming.
        
        Args:
            story_data: Datos de la historia de usuario
            callback: Función opcional para recibir chunks en tiempo real
            
        Returns:
            Análisis generado por la IA
        """
        try:
            prompt = self.create_analysis_prompt(story_data)
            
            # Definir el rol del sistema según el idioma
            system_role = self._get_system_role()
            
            response = completion(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=1200,
                stream=True
            )
            
            # Recolectar el contenido del stream
            full_content = ""
            for chunk in response:
                if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        full_content += delta.content
                        # Llamar callback si existe para actualizar UI en tiempo real
                        if callback:
                            callback(delta.content)
            
            return full_content
            
        except Exception as e:
            raise Exception(f"Error al analizar la historia: {str(e)}")
    
    def analyze_sprint(self, stories_data: list, callback=None) -> str:
        """
        Analiza múltiples historias como un sprint, identificando dependencias y generando plan de trabajo.
        
        Args:
            stories_data: Lista de datos de historias de usuario
            callback: Función opcional para recibir chunks en tiempo real
            
        Returns:
            Análisis consolidado del sprint
        """
        try:
            prompt = self._create_sprint_analysis_prompt(stories_data)
            system_role = self._get_sprint_system_role()
            
            response = completion(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=3000,  # Más tokens para análisis consolidado
                stream=True
            )
            
            # Recolectar el contenido del stream
            full_content = ""
            for chunk in response:
                if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        full_content += delta.content
                        if callback:
                            callback(delta.content)
            
            return full_content
            
        except Exception as e:
            raise Exception(f"Error analyzing sprint: {str(e)}")
    
    def _create_sprint_analysis_prompt(self, stories_data: list) -> str:
        """
        Crea prompt para análisis consolidado de sprint.
        
        Args:
            stories_data: Lista de historias del sprint
            
        Returns:
            Prompt formateado
        """
        if self.language == "es":
            return self._create_spanish_sprint_prompt(stories_data)
        else:
            return self._create_english_sprint_prompt(stories_data)
    
    def _create_english_sprint_prompt(self, stories_data: list) -> str:
        """Creates English prompt for sprint analysis."""
        
        # Build stories summary
        stories_summary = ""
        for i, story in enumerate(stories_data, 1):
            stories_summary += f"""
<story_{i}>
<metadata>
ID: {story['key']}
Title: {story['title']}
Priority: {story['priority']}
Status: {story['status']}
</metadata>
<description>
{story['description'] or 'No description'}
</description>
<acceptance_criteria>
{story['acceptance_criteria'] or 'No acceptance criteria'}
</acceptance_criteria>
</story_{i}>

"""
        
        prompt = f"""<task>
Analyze this sprint containing {len(stories_data)} user stories as a cohesive unit. Identify dependencies, conflicts, risks, and generate an implementation work plan.
</task>

<sprint_stories>
{stories_summary}
</sprint_stories>

<analysis_objectives>
1. UNDERSTAND SCOPE: What is the overall goal of this sprint?
2. IDENTIFY DEPENDENCIES: Which stories depend on others? (technical, data, or functional dependencies)
3. DETECT CONFLICTS: Are there overlapping functionalities or contradictions?
4. ASSESS RISKS: What could block or delay the sprint?
5. PRIORITIZE WORK: What's the optimal implementation order?
6. GENERATE PLAN: Create a concrete work plan with phases
</analysis_objectives>

<output_format>
## 1. SPRINT OVERVIEW

**Sprint Goal:** [Inferred overall objective]
**Total Stories:** {len(stories_data)}
**Complexity Assessment:** [High/Medium/Low with justification]

## 2. STORIES SUMMARY

| Story ID | Title | Priority | Complexity | Status |
|----------|-------|----------|------------|--------|
[Table with all stories]

## 3. DEPENDENCY ANALYSIS

**Technical Dependencies:**
- [Story A] → [Story B]: [Reason - e.g., "Story B requires API from Story A"]
- [Story C] → [Story D]: [Reason]

**Data Dependencies:**
- [Story X] → [Story Y]: [Reason - e.g., "Story Y needs data model from Story X"]

**Functional Dependencies:**
- [Story M] → [Story N]: [Reason - e.g., "Story N builds on feature from Story M"]

**Dependency Graph (ASCII):**
```
[Visual representation of dependencies]
```

## 4. CONFLICTS & OVERLAPS

**Potential Conflicts:**
- [Story A] vs [Story B]: [Description of conflict]

**Overlapping Functionality:**
- [Stories that might duplicate work]

**Recommendations:**
- [How to resolve conflicts]

## 5. RISK ASSESSMENT

**Critical Risks (High Impact):**
1. [Risk description] - Affects: [Story IDs] - Mitigation: [Strategy]
2. [Risk description] - Affects: [Story IDs] - Mitigation: [Strategy]

**Medium Risks:**
1. [Risk description] - Affects: [Story IDs] - Mitigation: [Strategy]

**Blockers:**
- [What could completely stop the sprint]

## 6. MISSING INFORMATION

**Critical Gaps Across Stories:**
- [Information needed before sprint starts]

**Per-Story Gaps:**
- {stories_data[0]['key']}: [Key missing info]
- [Continue for stories with significant gaps]

## 7. IMPLEMENTATION PLAN

**Phase 1: Foundation (Week 1)**
- Stories: [IDs]
- Rationale: [Why these first]
- Deliverables: [What will be ready]

**Phase 2: Core Features (Week 1-2)**
- Stories: [IDs]
- Rationale: [Why this order]
- Dependencies: [What from Phase 1 is needed]

**Phase 3: Integration (Week 2)**
- Stories: [IDs]
- Rationale: [Why these last]
- Integration Points: [What needs to connect]

**Phase 4: Polish & Testing (Week 2)**
- Stories: [IDs]
- Focus: [Final touches, edge cases]

## 8. RECOMMENDATIONS

**For Product Owner:**
1. [Recommendation about scope/priorities]
2. [Recommendation about missing info]

**For Development Team:**
1. [Technical recommendation]
2. [Architecture recommendation]

**For Sprint Success:**
1. [Process recommendation]
2. [Communication recommendation]

## 9. SUCCESS METRICS

**Definition of Done for Sprint:**
- [Criteria 1]
- [Criteria 2]

**Key Milestones:**
- Day 3: [Milestone]
- Day 7: [Milestone]
- Day 10: [Milestone]
</output_format>

<guidelines>
- Base analysis EXCLUSIVELY on provided stories
- Identify REAL dependencies (not assumed)
- Be specific about WHY stories depend on each other
- Prioritize based on dependencies and risk
- Provide actionable, concrete recommendations
- Consider team capacity and sprint timeline
- Flag any story that seems out of scope
</guidelines>"""

        return prompt
    
    def _create_spanish_sprint_prompt(self, stories_data: list) -> str:
        """Crea prompt en español para análisis de sprint."""
        
        # Build stories summary
        stories_summary = ""
        for i, story in enumerate(stories_data, 1):
            stories_summary += f"""
<historia_{i}>
<metadatos>
ID: {story['key']}
Título: {story['title']}
Prioridad: {story['priority']}
Estado: {story['status']}
</metadatos>
<descripcion>
{story['description'] or 'Sin descripción'}
</descripcion>
<criterios_aceptacion>
{story['acceptance_criteria'] or 'Sin criterios de aceptación'}
</criterios_aceptacion>
</historia_{i}>

"""
        
        prompt = f"""<tarea>
Analiza este sprint que contiene {len(stories_data)} historias de usuario como una unidad cohesiva. Identifica dependencias, conflictos, riesgos y genera un plan de trabajo de implementación.
</tarea>

<historias_sprint>
{stories_summary}
</historias_sprint>

<objetivos_analisis>
1. COMPRENDER ALCANCE: ¿Cuál es el objetivo general de este sprint?
2. IDENTIFICAR DEPENDENCIAS: ¿Qué historias dependen de otras? (dependencias técnicas, de datos o funcionales)
3. DETECTAR CONFLICTOS: ¿Hay funcionalidades superpuestas o contradicciones?
4. EVALUAR RIESGOS: ¿Qué podría bloquear o retrasar el sprint?
5. PRIORIZAR TRABAJO: ¿Cuál es el orden óptimo de implementación?
6. GENERAR PLAN: Crear un plan de trabajo concreto con fases
</objetivos_analisis>

<formato_salida>
## 1. RESUMEN DEL SPRINT

**Objetivo del Sprint:** [Objetivo general inferido]
**Total de Historias:** {len(stories_data)}
**Evaluación de Complejidad:** [Alta/Media/Baja con justificación]

## 2. RESUMEN DE HISTORIAS

| Story ID | Título | Prioridad | Complejidad | Estado |
|----------|--------|-----------|-------------|--------|
[Tabla con todas las historias]

## 3. ANÁLISIS DE DEPENDENCIAS

**Dependencias Técnicas:**
- [Historia A] → [Historia B]: [Razón - ej: "Historia B requiere API de Historia A"]
- [Historia C] → [Historia D]: [Razón]

**Dependencias de Datos:**
- [Historia X] → [Historia Y]: [Razón - ej: "Historia Y necesita modelo de datos de Historia X"]

**Dependencias Funcionales:**
- [Historia M] → [Historia N]: [Razón - ej: "Historia N se construye sobre funcionalidad de Historia M"]

**Grafo de Dependencias (ASCII):**
```
[Representación visual de dependencias]
```

## 4. CONFLICTOS Y SOLAPAMIENTOS

**Conflictos Potenciales:**
- [Historia A] vs [Historia B]: [Descripción del conflicto]

**Funcionalidad Superpuesta:**
- [Historias que podrían duplicar trabajo]

**Recomendaciones:**
- [Cómo resolver conflictos]

## 5. EVALUACIÓN DE RIESGOS

**Riesgos Críticos (Alto Impacto):**
1. [Descripción del riesgo] - Afecta: [IDs de historias] - Mitigación: [Estrategia]
2. [Descripción del riesgo] - Afecta: [IDs de historias] - Mitigación: [Estrategia]

**Riesgos Medios:**
1. [Descripción del riesgo] - Afecta: [IDs de historias] - Mitigación: [Estrategia]

**Bloqueadores:**
- [Qué podría detener completamente el sprint]

## 6. INFORMACIÓN FALTANTE

**Brechas Críticas Entre Historias:**
- [Información necesaria antes de iniciar el sprint]

**Brechas Por Historia:**
- {stories_data[0]['key']}: [Información clave faltante]
- [Continuar para historias con brechas significativas]

## 7. PLAN DE IMPLEMENTACIÓN

**Fase 1: Fundación (Semana 1)**
- Historias: [IDs]
- Justificación: [Por qué estas primero]
- Entregables: [Qué estará listo]

**Fase 2: Características Principales (Semana 1-2)**
- Historias: [IDs]
- Justificación: [Por qué este orden]
- Dependencias: [Qué de Fase 1 se necesita]

**Fase 3: Integración (Semana 2)**
- Historias: [IDs]
- Justificación: [Por qué estas al final]
- Puntos de Integración: [Qué necesita conectarse]

**Fase 4: Pulido y Pruebas (Semana 2)**
- Historias: [IDs]
- Enfoque: [Toques finales, casos edge]

## 8. RECOMENDACIONES

**Para el Product Owner:**
1. [Recomendación sobre alcance/prioridades]
2. [Recomendación sobre información faltante]

**Para el Equipo de Desarrollo:**
1. [Recomendación técnica]
2. [Recomendación de arquitectura]

**Para Éxito del Sprint:**
1. [Recomendación de proceso]
2. [Recomendación de comunicación]

## 9. MÉTRICAS DE ÉXITO

**Definición de Terminado para el Sprint:**
- [Criterio 1]
- [Criterio 2]

**Hitos Clave:**
- Día 3: [Hito]
- Día 7: [Hito]
- Día 10: [Hito]
</formato_salida>

<directrices>
- Basa el análisis EXCLUSIVAMENTE en las historias proporcionadas
- Identifica dependencias REALES (no asumidas)
- Sé específico sobre POR QUÉ las historias dependen entre sí
- Prioriza basándote en dependencias y riesgo
- Proporciona recomendaciones concretas y accionables
- Considera capacidad del equipo y timeline del sprint
- Señala cualquier historia que parezca fuera de alcance
</directrices>"""

        return prompt
    
    def _get_sprint_system_role(self) -> str:
        """Obtiene el rol del sistema para análisis de sprint."""
        if self.language == "es":
            return """Eres un arquitecto de software senior y Scrum Master especializado en planificación de sprints y análisis de dependencias entre historias de usuario.

REGLA CRÍTICA: Analiza las historias como un conjunto cohesivo. Identifica dependencias REALES basadas en la información proporcionada. NO inventes dependencias o asumas información que no está presente. Genera un plan de trabajo práctico y realista."""
        else:
            return """You are a senior software architect and Scrum Master specialized in sprint planning and analyzing dependencies between user stories.

CRITICAL RULE: Analyze stories as a cohesive set. Identify REAL dependencies based on provided information. DO NOT invent dependencies or assume information not present. Generate a practical and realistic work plan."""
    
    def generate_test_cases(self, story_data: Dict[str, Any], callback=None) -> str:
        """
        Genera test cases en formato Gherkin basados en la historia de usuario.
        
        Args:
            story_data: Datos de la historia de usuario
            callback: Función opcional para recibir chunks en tiempo real
            
        Returns:
            Test cases en formato Gherkin
        """
        try:
            prompt = self._create_test_cases_prompt(story_data)
            system_role = self._get_test_cases_system_role()
            
            response = completion(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=2000,
                stream=True
            )
            
            # Recolectar el contenido del stream
            full_content = ""
            for chunk in response:
                if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        full_content += delta.content
                        if callback:
                            callback(delta.content)
            
            return full_content
            
        except Exception as e:
            raise Exception(f"Error generating test cases: {str(e)}")
    
    def _create_test_cases_prompt(self, story_data: Dict[str, Any]) -> str:
        """Crea prompt para generar test cases."""
        if self.language == "es":
            return self._create_spanish_test_cases_prompt(story_data)
        else:
            return self._create_english_test_cases_prompt(story_data)
    
    def _create_english_test_cases_prompt(self, story_data: Dict[str, Any]) -> str:
        """Creates English prompt for test case generation."""
        
        prompt = f"""<task>
Generate comprehensive test cases in Gherkin format (Given-When-Then) for the following user story.
</task>

<story_data>
<metadata>
ID: {story_data['key']}
Title: {story_data['title']}
Priority: {story_data['priority']}
</metadata>

<description>
{story_data['description'] or 'No description'}
{f"\\n--- ANALYST NOTES ---\\n{story_data['user_notes']}\\n--- END NOTES ---" if story_data.get('user_notes') else ''}
</description>

<acceptance_criteria>
{story_data['acceptance_criteria'] or 'No acceptance criteria'}
</acceptance_criteria>
</story_data>

<output_format>
Generate test cases in standard Gherkin format:

Feature: [Feature name from story]
  As a [user type]
  I want [functionality]
  So that [business value]

  Background:
    Given [common preconditions for all scenarios]

  Scenario: [Scenario name - Happy Path]
    Given [precondition]
    And [another precondition]
    When [action]
    And [another action]
    Then [expected result]
    And [another expected result]

  Scenario: [Scenario name - Edge Case]
    Given [precondition]
    When [action]
    Then [expected result]

  Scenario: [Scenario name - Error Handling]
    Given [precondition]
    When [invalid action]
    Then [error handling result]
</output_format>

<test_coverage_requirements>
Generate test cases for:

1. **Happy Path Scenarios** (2-3 scenarios)
   - Main user flow with valid inputs
   - Expected successful outcomes
   - Core functionality working as intended

2. **Edge Cases** (2-3 scenarios)
   - Boundary conditions
   - Minimum/maximum values
   - Empty or null inputs
   - Special characters
   - Large data sets

3. **Error Scenarios** (2-3 scenarios)
   - Invalid inputs
   - Missing required fields
   - Unauthorized access
   - System errors
   - Timeout scenarios

4. **Validation Tests** (1-2 scenarios)
   - Input validation
   - Business rule validation
   - Data format validation

5. **Integration Tests** (if applicable, 1-2 scenarios)
   - API interactions
   - Database operations
   - Third-party service calls
</test_coverage_requirements>

<guidelines>
- Use clear, specific language in Gherkin steps
- Each scenario should be independent and executable
- Use "And" for multiple steps of the same type
- Include specific data values in examples when relevant
- Focus on behavior, not implementation
- Base test cases ONLY on information in the story
- DO NOT invent features or functionality not mentioned
- If acceptance criteria are vague, note it in comments
- Use realistic test data
- Keep scenarios focused and atomic
</guidelines>

<example_quality>
Good:
  Scenario: User successfully logs in with valid credentials
    Given the user is on the login page
    And the user has a valid account with email "user@example.com"
    When the user enters email "user@example.com"
    And the user enters password "ValidPass123"
    And the user clicks the "Login" button
    Then the user should be redirected to the dashboard
    And the user should see a welcome message "Welcome back, User"

Bad:
  Scenario: Login works
    Given user on page
    When user logs in
    Then success
</example_quality>"""

        return prompt
    
    def _create_spanish_test_cases_prompt(self, story_data: Dict[str, Any]) -> str:
        """Crea prompt en español para generación de test cases."""
        
        prompt = f"""<tarea>
Genera casos de prueba completos en formato Gherkin (Dado-Cuando-Entonces) para la siguiente historia de usuario.
</tarea>

<datos_historia>
<metadatos>
ID: {story_data['key']}
Título: {story_data['title']}
Prioridad: {story_data['priority']}
</metadatos>

<descripcion>
{story_data['description'] or 'Sin descripción'}
{f"\\n--- NOTAS DEL ANALISTA ---\\n{story_data['user_notes']}\\n--- FIN NOTAS ---" if story_data.get('user_notes') else ''}
</descripcion>

<criterios_aceptacion>
{story_data['acceptance_criteria'] or 'Sin criterios de aceptación'}
</criterios_aceptacion>
</datos_historia>

<formato_salida>
Genera casos de prueba en formato Gherkin estándar:

Característica: [Nombre de la característica]
  Como [tipo de usuario]
  Quiero [funcionalidad]
  Para [valor de negocio]

  Antecedentes:
    Dado [precondiciones comunes para todos los escenarios]

  Escenario: [Nombre del escenario - Flujo Principal]
    Dado [precondición]
    Y [otra precondición]
    Cuando [acción]
    Y [otra acción]
    Entonces [resultado esperado]
    Y [otro resultado esperado]

  Escenario: [Nombre del escenario - Caso Límite]
    Dado [precondición]
    Cuando [acción]
    Entonces [resultado esperado]

  Escenario: [Nombre del escenario - Manejo de Errores]
    Dado [precondición]
    Cuando [acción inválida]
    Entonces [resultado de manejo de error]
</formato_salida>

<requisitos_cobertura>
Genera casos de prueba para:

1. **Escenarios de Flujo Principal** (2-3 escenarios)
   - Flujo principal con entradas válidas
   - Resultados exitosos esperados
   - Funcionalidad principal funcionando correctamente

2. **Casos Límite** (2-3 escenarios)
   - Condiciones de frontera
   - Valores mínimos/máximos
   - Entradas vacías o nulas
   - Caracteres especiales
   - Conjuntos de datos grandes

3. **Escenarios de Error** (2-3 escenarios)
   - Entradas inválidas
   - Campos requeridos faltantes
   - Acceso no autorizado
   - Errores del sistema
   - Escenarios de timeout

4. **Pruebas de Validación** (1-2 escenarios)
   - Validación de entrada
   - Validación de reglas de negocio
   - Validación de formato de datos

5. **Pruebas de Integración** (si aplica, 1-2 escenarios)
   - Interacciones con API
   - Operaciones de base de datos
   - Llamadas a servicios de terceros
</requisitos_cobertura>

<directrices>
- Usa lenguaje claro y específico en los pasos Gherkin
- Cada escenario debe ser independiente y ejecutable
- Usa "Y" para múltiples pasos del mismo tipo
- Incluye valores de datos específicos en ejemplos cuando sea relevante
- Enfócate en comportamiento, no en implementación
- Basa los casos de prueba SOLO en información de la historia
- NO inventes características o funcionalidad no mencionada
- Si los criterios de aceptación son vagos, nótalo en comentarios
- Usa datos de prueba realistas
- Mantén los escenarios enfocados y atómicos
</directrices>

<ejemplo_calidad>
Bueno:
  Escenario: Usuario inicia sesión exitosamente con credenciales válidas
    Dado que el usuario está en la página de inicio de sesión
    Y el usuario tiene una cuenta válida con email "usuario@ejemplo.com"
    Cuando el usuario ingresa el email "usuario@ejemplo.com"
    Y el usuario ingresa la contraseña "ClaveValida123"
    Y el usuario hace clic en el botón "Iniciar Sesión"
    Entonces el usuario debe ser redirigido al dashboard
    Y el usuario debe ver un mensaje de bienvenida "Bienvenido de nuevo, Usuario"

Malo:
  Escenario: Login funciona
    Dado usuario en página
    Cuando usuario inicia sesión
    Entonces éxito
</ejemplo_calidad>"""

        return prompt
    
    def _get_test_cases_system_role(self) -> str:
        """Obtiene el rol del sistema para generación de test cases."""
        if self.language == "es":
            return """Eres un QA Engineer senior especializado en crear casos de prueba completos y ejecutables en formato Gherkin.

REGLA CRÍTICA: Genera casos de prueba basados EXCLUSIVAMENTE en la información proporcionada en la historia de usuario. NO inventes funcionalidad o comportamientos no mencionados. Crea escenarios claros, específicos y ejecutables que cubran flujos principales, casos límite y manejo de errores."""
        else:
            return """You are a senior QA Engineer specialized in creating comprehensive and executable test cases in Gherkin format.

CRITICAL RULE: Generate test cases based EXCLUSIVELY on information provided in the user story. DO NOT invent functionality or behaviors not mentioned. Create clear, specific, and executable scenarios covering happy paths, edge cases, and error handling."""
    
    def followup_question(self, story_data: Dict[str, Any], conversation_history: list, question: str, callback=None) -> str:
        """
        Procesa una pregunta de seguimiento sobre el análisis.
        
        Args:
            story_data: Datos originales de la historia
            conversation_history: Historial de la conversación
            question: Pregunta del usuario
            callback: Función opcional para recibir chunks en tiempo real
            
        Returns:
            Respuesta de la IA
        """
        try:
            # Construir contexto para la pregunta de seguimiento
            system_role = self._get_system_role()
            
            # Crear contexto de la historia
            story_context = f"""Story ID: {story_data['key']}
Title: {story_data['title']}
Description: {story_data.get('description', 'N/A')}
Acceptance Criteria: {story_data.get('acceptance_criteria', 'N/A')}"""
            
            # Construir mensajes
            messages = [
                {"role": "system", "content": system_role},
                {"role": "system", "content": f"Context - You are discussing this user story:\n\n{story_context}"}
            ]
            
            # Agregar historial de conversación
            messages.extend(conversation_history)
            
            # Agregar pregunta actual
            messages.append({"role": "user", "content": question})
            
            response = completion(
                model=self.model,
                messages=messages,
                temperature=0.2,
                max_tokens=1200,
                stream=True
            )
            
            # Recolectar el contenido del stream
            full_content = ""
            for chunk in response:
                if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                    delta = chunk.choices[0].delta
                    if hasattr(delta, 'content') and delta.content:
                        full_content += delta.content
                        if callback:
                            callback(delta.content)
            
            return full_content
            
        except Exception as e:
            raise Exception(f"Error processing follow-up question: {str(e)}")
    
    def _get_system_role(self) -> str:
        """Obtiene el rol del sistema según el idioma."""
        if self.language == "es":
            return """Eres un arquitecto de software senior y un ingeniero de QA especializado en analizar historias de usuario de Jira e identificar requisitos faltantes y casos de prueba. 

REGLA CRÍTICA: Antes de producir la respuesta final, razona cuidadosamente sobre los requisitos y posibles ambigüedades. Basa tu análisis ÚNICAMENTE en la información explícitamente proporcionada en el story. NO inventes, asumas o agregues información que no esté presente en el texto. Usa SOLO los términos y conceptos mencionados en el story y las notas del analista."""
        else:
            return """You are a senior software architect and QA engineer specialized in analyzing Jira user stories and identifying missing requirements and test cases. 

CRITICAL RULE: Before producing the final answer, carefully reason about the requirements and possible ambiguities. Base your analysis EXCLUSIVELY on information explicitly provided in the story. DO NOT invent, assume, or add information that is not present in the text. Use ONLY the terms and concepts mentioned in the story and analyst notes."""
