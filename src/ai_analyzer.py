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
Provide a concise, actionable analysis using this exact structure:

## 1. QUICK SUMMARY

**User Story:** As a [who], I want [what], so that [why]
**Business Value:** [One sentence - why this matters]
**Complexity:** [Low/Medium/High] - [Brief justification]

## 2. WHAT TO BUILD

**Core Features:**
- [Feature 1: Clear, specific description]
- [Feature 2: Clear, specific description]
- [Feature 3: Clear, specific description]

**Key User Interactions:**
- [How users will interact - be specific]

**Expected Outcome:**
- [What should happen when it works correctly]

## 3. CRITICAL GAPS

**❌ Blockers (Must resolve before starting):**
- [Critical missing information that prevents development]
- [Another blocker if exists, otherwise "None identified"]

**⚠️ Risks (Could cause problems):**
- [Risk 1]: [Why it's a risk]
- [Risk 2]: [Why it's a risk]

**ℹ️ Key Questions:**
1. [Specific question for Product Owner]
2. [Specific question for Technical Team]
3. [Specific question about edge cases/validation]

## 4. TECHNICAL TASKS

**Backend:**
- [ ] [Task 1: Specific backend task]
- [ ] [Task 2: Specific backend task]

**Frontend:**
- [ ] [Task 1: Specific frontend task]
- [ ] [Task 2: Specific frontend task]

**Database:**
- [ ] [Task 1: Specific database task]
- [ ] [Task 2: Specific database task]

**Testing:**
- [ ] [Task 1: Specific testing task]
- [ ] [Task 2: Specific testing task]

**DevOps/Infrastructure:**
- [ ] [Task 1: If applicable, otherwise "Not applicable"]

## 5. NEXT STEPS

**For Product Owner:**
- [ ] [Specific action item 1]
- [ ] [Specific action item 2]

**For Dev Team:**
- [ ] [Specific action item 1]
- [ ] [Specific action item 2]

**Ready to Start?** [YES/NO]
- [If NO: Brief reason why not ready]
- [If YES: Any important considerations before starting]
</output_format>

<guidelines>
- Be CONCISE - each section should be scannable in seconds
- Focus on ACTIONABLE information only
- Use bullet points, not paragraphs
- Limit to 3-5 items per section (only the most important)
- Be SPECIFIC - avoid vague statements
- Prioritize what blocks or risks development
- Questions should be answerable and specific
- Technical tasks should be CONCRETE and IMPLEMENTABLE
- Each task should be small enough to complete in 1-4 hours
- Tasks should follow a logical implementation order

CRITICAL ANTI-HALLUCINATION RULES:
- Base analysis EXCLUSIVELY on information explicitly provided in the story
- DO NOT invent features, requirements, or technical details not mentioned
- Use ONLY exact terms and language from the story itself
- If suggesting something new, clearly mark it as "RECOMMENDATION"
- When in doubt, point out what's missing rather than filling gaps with assumptions
- Technical tasks must be based ONLY on explicitly mentioned functionality

CONSTRUCTIVE APPROACH:
- Start with what's clear and well-defined
- Extract key points and make them prominent
- Identify gaps in a helpful, specific manner
- Provide actionable next steps, not just criticism
- Break down work into concrete, implementable tasks
</guidelines>

<example_quality>
Good Technical Task: "[ ] Create POST /api/users endpoint with email validation"
Bad Technical Task: "[ ] Implement user functionality"

Good Technical Task: "[ ] Add user_email column to users table with unique constraint"
Bad Technical Task: "[ ] Update database"

Good: "❌ Blocker: Error handling not specified. What should happen if payment gateway times out?"
Bad: "Error handling needs work."

Good: "⚠️ Risk: No performance requirements. With 10k+ users, response time could be unacceptable."
Bad: "Performance not mentioned."

Good: "For Product Owner: [ ] Define maximum file upload size and supported formats"
Bad: "Clarify requirements"
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
Proporciona un análisis conciso y accionable usando esta estructura exacta:

## 1. RESUMEN RÁPIDO

**Historia de Usuario:** Como [quién], quiero [qué], para [por qué]
**Valor de Negocio:** [Una oración - por qué esto importa]
**Complejidad:** [Baja/Media/Alta] - [Breve justificación]

## 2. QUÉ CONSTRUIR

**Características Principales:**
- [Característica 1: Descripción clara y específica]
- [Característica 2: Descripción clara y específica]
- [Característica 3: Descripción clara y específica]

**Interacciones Clave del Usuario:**
- [Cómo los usuarios interactuarán - ser específico]

**Resultado Esperado:**
- [Qué debería suceder cuando funcione correctamente]

## 3. BRECHAS CRÍTICAS

**❌ Bloqueadores (Deben resolverse antes de empezar):**
- [Información crítica faltante que impide el desarrollo]
- [Otro bloqueador si existe, sino "Ninguno identificado"]

**⚠️ Riesgos (Podrían causar problemas):**
- [Riesgo 1]: [Por qué es un riesgo]
- [Riesgo 2]: [Por qué es un riesgo]

**ℹ️ Preguntas Clave:**
1. [Pregunta específica para Product Owner]
2. [Pregunta específica para Equipo Técnico]
3. [Pregunta específica sobre casos edge/validación]

## 4. TAREAS TÉCNICAS

**Backend:**
- [ ] [Tarea 1: Tarea específica de backend]
- [ ] [Tarea 2: Tarea específica de backend]

**Frontend:**
- [ ] [Tarea 1: Tarea específica de frontend]
- [ ] [Tarea 2: Tarea específica de frontend]

**Base de Datos:**
- [ ] [Tarea 1: Tarea específica de base de datos]
- [ ] [Tarea 2: Tarea específica de base de datos]

**Testing:**
- [ ] [Tarea 1: Tarea específica de testing]
- [ ] [Tarea 2: Tarea específica de testing]

**DevOps/Infraestructura:**
- [ ] [Tarea 1: Si aplica, sino "No aplica"]

## 5. PRÓXIMOS PASOS

**Para el Product Owner:**
- [ ] [Acción específica 1]
- [ ] [Acción específica 2]

**Para el Equipo de Desarrollo:**
- [ ] [Acción específica 1]
- [ ] [Acción específica 2]

**¿Listo para Empezar?** [SÍ/NO]
- [Si NO: Breve razón por qué no está listo]
- [Si SÍ: Consideraciones importantes antes de empezar]
</formato_salida>

<directrices>
- Sé CONCISO - cada sección debe ser escaneable en segundos
- Enfócate en información ACCIONABLE solamente
- Usa viñetas, no párrafos
- Limita a 3-5 elementos por sección (solo lo más importante)
- Sé ESPECÍFICO - evita declaraciones vagas
- Prioriza lo que bloquea o arriesga el desarrollo
- Las preguntas deben ser respondibles y específicas
- Las tareas técnicas deben ser CONCRETAS e IMPLEMENTABLES
- Cada tarea debe ser lo suficientemente pequeña para completarse en 1-4 horas
- Las tareas deben seguir un orden lógico de implementación

REGLAS CRÍTICAS ANTI-ALUCINACIÓN:
- Basa el análisis EXCLUSIVAMENTE en información explícitamente proporcionada en la historia
- NO inventes características, requisitos o detalles técnicos no mencionados
- Usa ÚNICAMENTE términos exactos y lenguaje de la historia misma
- Si sugieres algo nuevo, márcalo claramente como "RECOMENDACIÓN"
- Cuando tengas dudas, señala lo que falta en lugar de llenar vacíos con suposiciones
- Las tareas técnicas deben basarse SOLO en funcionalidad explícitamente mencionada

ENFOQUE CONSTRUCTIVO:
- Comienza con lo que está claro y bien definido
- Extrae puntos clave y hazlos prominentes
- Identifica brechas de manera útil y específica
- Proporciona próximos pasos accionables, no solo críticas
- Descompone el trabajo en tareas concretas e implementables
</directrices>

<ejemplo_calidad>
Buena Tarea Técnica: "[ ] Crear endpoint POST /api/usuarios con validación de email"
Mala Tarea Técnica: "[ ] Implementar funcionalidad de usuario"

Buena Tarea Técnica: "[ ] Agregar columna email_usuario a tabla usuarios con constraint unique"
Mala Tarea Técnica: "[ ] Actualizar base de datos"

Bueno: "❌ Bloqueador: Manejo de errores no especificado. ¿Qué debería suceder si el gateway de pago expira?"
Malo: "El manejo de errores necesita trabajo."

Bueno: "⚠️ Riesgo: Sin requisitos de rendimiento. Con 10k+ usuarios, el tiempo de respuesta podría ser inaceptable."
Malo: "No se menciona el rendimiento."

Bueno: "Para Product Owner: [ ] Definir tamaño máximo de archivo y formatos soportados"
Malo: "Aclarar requisitos"
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
