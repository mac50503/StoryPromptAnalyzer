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
