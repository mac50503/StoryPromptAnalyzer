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

## 2. REQUIREMENT STRUCTURE

**Actors:** [Comma-separated list]

**Main Flow:**
1. [Step 1]
2. [Step 2]
...

**Dependencies:**
- Technical: [List or "None identified"]
- Business: [List or "None identified"]

## 3. DETECTED AMBIGUITIES

**Critical (Must clarify before development):**
- [Item 1]
- [Item 2]

**Minor (Should clarify but not blocking):**
- [Item 1]

**Vague Terms Requiring Definition:**
- "[term]": [Why it's vague]

## 4. MISSING INFORMATION

**Acceptance Criteria Gaps:**
- [Specific gap 1]
- [Specific gap 2]

**Unaddressed Edge Cases:**
- [Case 1: Description]
- [Case 2: Description]

**Non-Functional Requirements:**
- Performance: [What's missing or "Not specified"]
- Security: [What's missing or "Not specified"]
- Scalability: [What's missing or "Not specified"]
- Accessibility: [What's missing or "Not specified"]

**Data Requirements:**
- [What data/context is needed]

## 5. CLARIFICATION QUESTIONS

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

## 6. RECOMMENDATIONS

**Immediate Actions (Before Development):**
- [Action 1 with rationale]
- [Action 2 with rationale]

**Quality Improvements:**
- [Improvement 1]
- [Improvement 2]

**Risk Mitigation:**
- [Risk 1]: [Mitigation strategy]
- [Risk 2]: [Mitigation strategy]

**Alternative Approaches:**
- [Alternative 1]: [When to consider]
</output_format>

<guidelines>
- Be specific and actionable in all recommendations
- Prioritize critical issues that block development
- Provide concrete examples when identifying problems
- Focus on what's missing or unclear, not what's already clear
- Use bullet points for lists, numbered lists for sequences
- If something is well-defined, acknowledge it briefly and move on
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

## 2. ESTRUCTURA DEL REQUERIMIENTO

**Actores:** [Lista separada por comas]

**Flujo Principal:**
1. [Paso 1]
2. [Paso 2]
...

**Dependencias:**
- Técnicas: [Lista o "Ninguna identificada"]
- De Negocio: [Lista o "Ninguna identificada"]

## 3. AMBIGÜEDADES DETECTADAS

**Críticas (Deben aclararse antes del desarrollo):**
- [Elemento 1]
- [Elemento 2]

**Menores (Deberían aclararse pero no bloquean):**
- [Elemento 1]

**Términos Vagos que Requieren Definición:**
- "[término]": [Por qué es vago]

## 4. INFORMACIÓN FALTANTE

**Brechas en Criterios de Aceptación:**
- [Brecha específica 1]
- [Brecha específica 2]

**Casos Edge No Abordados:**
- [Caso 1: Descripción]
- [Caso 2: Descripción]

**Requisitos No Funcionales:**
- Rendimiento: [Qué falta o "No especificado"]
- Seguridad: [Qué falta o "No especificado"]
- Escalabilidad: [Qué falta o "No especificado"]
- Accesibilidad: [Qué falta o "No especificado"]

**Requisitos de Datos:**
- [Qué datos/contexto se necesita]

## 5. PREGUNTAS DE CLARIFICACIÓN

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

## 6. RECOMENDACIONES

**Acciones Inmediatas (Antes del Desarrollo):**
- [Acción 1 con justificación]
- [Acción 2 con justificación]

**Mejoras de Calidad:**
- [Mejora 1]
- [Mejora 2]

**Mitigación de Riesgos:**
- [Riesgo 1]: [Estrategia de mitigación]
- [Riesgo 2]: [Estrategia de mitigación]

**Enfoques Alternativos:**
- [Alternativa 1]: [Cuándo considerarla]
</formato_salida>

<directrices>
- Sé específico y accionable en todas las recomendaciones
- Prioriza problemas críticos que bloquean el desarrollo
- Proporciona ejemplos concretos al identificar problemas
- Enfócate en lo que falta o no está claro, no en lo que ya está claro
- Usa viñetas para listas, listas numeradas para secuencias
- Si algo está bien definido, reconócelo brevemente y continúa
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
