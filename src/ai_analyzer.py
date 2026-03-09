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
        """Crea el prompt en inglés usando técnicas avanzadas de prompt engineering."""
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

2. DECOMPOSE: Break down the requirement
   - What are the main components?
   - What are the dependencies?
   - What are the success criteria?

3. IDENTIFY GAPS: Look for missing information
   - What assumptions are implicit?
   - What edge cases exist?
   - What could go wrong?

4. ASSESS QUALITY: Evaluate completeness
   - Are criteria SMART and testable?
   - Are non-functional requirements addressed?
   - Is the scope clear?

5. FORMULATE QUESTIONS: What needs clarification?
   - Business logic questions
   - Technical implementation questions
   - Testing and validation questions
</analysis_methodology>

<output_format>
Provide your analysis using this exact structure:

## 1. REQUIREMENT SUMMARY
<summary>
User Story: As a [who], I want [what], so that [why]
Business Value: [One sentence describing business impact]
Core Functionality: [2-3 sentences describing main feature]
</summary>

## 2. REQUIREMENT STRUCTURE
<structure>
Actors: [Comma-separated list]
Main Flow:
1. [Step 1]
2. [Step 2]
...

Dependencies:
- Technical: [List or "None identified"]
- Business: [List or "None identified"]
</structure>

## 3. DETECTED AMBIGUITIES
<ambiguities>
Critical (Must clarify before development):
- [Item 1]
- [Item 2]

Minor (Should clarify but not blocking):
- [Item 1]

Vague Terms Requiring Definition:
- "[term]": [Why it's vague]
</ambiguities>

## 4. MISSING INFORMATION
<missing_info>
Acceptance Criteria Gaps:
- [Specific gap 1]
- [Specific gap 2]

Unaddressed Edge Cases:
- [Case 1: Description]
- [Case 2: Description]

Non-Functional Requirements:
- Performance: [What's missing or "Not specified"]
- Security: [What's missing or "Not specified"]
- Scalability: [What's missing or "Not specified"]
- Accessibility: [What's missing or "Not specified"]

Data Requirements:
- [What data/context is needed]
</missing_info>

## 5. CLARIFICATION QUESTIONS
<questions>
For Product Owner:
1. [Specific question about business logic]
2. [Specific question about user experience]
3. [Specific question about priorities]

For Technical Team:
1. [Specific question about implementation]
2. [Specific question about integration]
3. [Specific question about constraints]

For QA/Testing:
1. [Specific question about test scenarios]
2. [Specific question about error handling]
3. [Specific question about validation]
</questions>

## 6. RECOMMENDATIONS
<recommendations>
Immediate Actions (Before Development):
- [Action 1 with rationale]
- [Action 2 with rationale]

Quality Improvements:
- [Improvement 1]
- [Improvement 2]

Risk Mitigation:
- [Risk 1]: [Mitigation strategy]
- [Risk 2]: [Mitigation strategy]

Alternative Approaches:
- [Alternative 1]: [When to consider]
</recommendations>
</output_format>

<guidelines>
- Be specific and actionable in all recommendations
- Prioritize critical issues that block development
- Provide concrete examples when identifying problems
- Focus on what's missing or unclear, not what's already clear
- Use bullet points for lists, numbered lists for sequences
- If something is well-defined, acknowledge it briefly and move on
- Limit each section to the most important 3-5 items
- CRITICAL: Base your analysis ONLY on information explicitly provided in the story data above
- DO NOT hallucinate or invent features, requirements, or technical details not mentioned in the story
- When referencing functionality, use ONLY the exact terms and language from the story itself
- If you need to suggest something, clearly mark it as a recommendation, not as existing functionality
</guidelines>

<example_quality>
Good: "The error handling for invalid user input is not specified. What should happen if the user enters a negative quantity?"
Bad: "Error handling needs work."

Good: "Performance requirement missing: What is the acceptable response time for search queries with 10,000+ results?"
Bad: "Performance not mentioned."
</example_quality>"""

        return prompt
    
    def _create_spanish_prompt(self, story_data: Dict[str, Any]) -> str:
        """Crea el prompt en español usando técnicas avanzadas de prompt engineering."""
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

2. DESCOMPONER: Desglosa el requerimiento
   - ¿Cuáles son los componentes principales?
   - ¿Cuáles son las dependencias?
   - ¿Cuáles son los criterios de éxito?

3. IDENTIFICAR BRECHAS: Busca información faltante
   - ¿Qué suposiciones son implícitas?
   - ¿Qué casos edge existen?
   - ¿Qué podría salir mal?

4. EVALUAR CALIDAD: Evalúa la completitud
   - ¿Los criterios son SMART y verificables?
   - ¿Se abordan los requisitos no funcionales?
   - ¿El alcance está claro?

5. FORMULAR PREGUNTAS: ¿Qué necesita aclaración?
   - Preguntas de lógica de negocio
   - Preguntas de implementación técnica
   - Preguntas de pruebas y validación
</metodologia_analisis>

<formato_salida>
Proporciona tu análisis usando esta estructura exacta:

## 1. RESUMEN DEL REQUERIMIENTO
<resumen>
Historia de Usuario: Como [quién], quiero [qué], para [por qué]
Valor de Negocio: [Una oración describiendo el impacto de negocio]
Funcionalidad Principal: [2-3 oraciones describiendo la característica principal]
</resumen>

## 2. ESTRUCTURA DEL REQUERIMIENTO
<estructura>
Actores: [Lista separada por comas]
Flujo Principal:
1. [Paso 1]
2. [Paso 2]
...

Dependencias:
- Técnicas: [Lista o "Ninguna identificada"]
- De Negocio: [Lista o "Ninguna identificada"]
</estructura>

## 3. AMBIGÜEDADES DETECTADAS
<ambiguedades>
Críticas (Deben aclararse antes del desarrollo):
- [Elemento 1]
- [Elemento 2]

Menores (Deberían aclararse pero no bloquean):
- [Elemento 1]

Términos Vagos que Requieren Definición:
- "[término]": [Por qué es vago]
</ambiguedades>

## 4. INFORMACIÓN FALTANTE
<informacion_faltante>
Brechas en Criterios de Aceptación:
- [Brecha específica 1]
- [Brecha específica 2]

Casos Edge No Abordados:
- [Caso 1: Descripción]
- [Caso 2: Descripción]

Requisitos No Funcionales:
- Rendimiento: [Qué falta o "No especificado"]
- Seguridad: [Qué falta o "No especificado"]
- Escalabilidad: [Qué falta o "No especificado"]
- Accesibilidad: [Qué falta o "No especificado"]

Requisitos de Datos:
- [Qué datos/contexto se necesita]
</informacion_faltante>

## 5. PREGUNTAS DE CLARIFICACIÓN
<preguntas>
Para el Product Owner:
1. [Pregunta específica sobre lógica de negocio]
2. [Pregunta específica sobre experiencia de usuario]
3. [Pregunta específica sobre prioridades]

Para el Equipo Técnico:
1. [Pregunta específica sobre implementación]
2. [Pregunta específica sobre integración]
3. [Pregunta específica sobre restricciones]

Para QA/Testing:
1. [Pregunta específica sobre escenarios de prueba]
2. [Pregunta específica sobre manejo de errores]
3. [Pregunta específica sobre validación]
</preguntas>

## 6. RECOMENDACIONES
<recomendaciones>
Acciones Inmediatas (Antes del Desarrollo):
- [Acción 1 con justificación]
- [Acción 2 con justificación]

Mejoras de Calidad:
- [Mejora 1]
- [Mejora 2]

Mitigación de Riesgos:
- [Riesgo 1]: [Estrategia de mitigación]
- [Riesgo 2]: [Estrategia de mitigación]

Enfoques Alternativos:
- [Alternativa 1]: [Cuándo considerarla]
</recomendaciones>
</formato_salida>

<directrices>
- Sé específico y accionable en todas las recomendaciones
- Prioriza problemas críticos que bloquean el desarrollo
- Proporciona ejemplos concretos al identificar problemas
- Enfócate en lo que falta o no está claro, no en lo que ya está claro
- Usa viñetas para listas, listas numeradas para secuencias
- Si algo está bien definido, reconócelo brevemente y continúa
- Limita cada sección a los 3-5 elementos más importantes
- CRÍTICO: Basa tu análisis ÚNICAMENTE en la información explícitamente proporcionada en los datos de la historia
- NO alucines ni inventes características, requisitos o detalles técnicos que no se mencionan en la historia
- Al referenciar funcionalidad, usa ÚNICAMENTE los términos exactos y el lenguaje de la historia misma
- Si necesitas sugerir algo, márcalo claramente como una recomendación, no como funcionalidad existente
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
    
    def _get_system_role(self) -> str:
        """Obtiene el rol del sistema según el idioma."""
        if self.language == "es":
            return "Eres un arquitecto de software senior y un ingeniero de QA especializado en analizar historias de usuario de Jira e identificar requisitos faltantes y casos de prueba. Antes de producir la respuesta final, razona cuidadosamente sobre los requisitos y posibles ambigüedades."
        else:
            return "You are a senior software architect and QA engineer specialized in analyzing Jira user stories and identifying missing requirements and test cases. Before producing the final answer, carefully reason about the requirements and possible ambiguities."
