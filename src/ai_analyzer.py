"""Analizador de historias de usuario usando IA."""

from typing import Dict, Any
import os
from litellm import completion


class AIAnalyzer:
    """Analizador de requerimientos usando modelos de IA."""

    def __init__(self, model: str = "gpt-4"):
        """
        Inicializa el analizador.
        
        Args:
            model: Modelo de IA a usar (ej: gpt-4, claude-3-opus-20240229)
        """
        self.model = model
        
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
        prompt = f"""Eres un experto en desarrollo y arquitectura de software con amplia experiencia en análisis de requerimientos y mejores prácticas de ingeniería.

Tu tarea es analizar la siguiente historia de usuario de Jira y proporcionar un análisis detallado.

**HISTORIA DE USUARIO:**

**ID:** {story_data['key']}
**Título:** {story_data['title']}
**Estado:** {story_data['status']}
**Prioridad:** {story_data['priority']}

**Descripción:**
{story_data['description']}

**Criterios de Aceptación:**
{story_data['acceptance_criteria'] or 'No especificados'}

**Etiquetas:** {', '.join(story_data['labels']) if story_data['labels'] else 'Ninguna'}

**Comentarios:**
{self._format_comments(story_data['comments'])}

---

**ANÁLISIS REQUERIDO:**

Por favor, proporciona un análisis estructurado que incluya:

1. **RESUMEN DEL REQUERIMIENTO**
   - Reformula el requerimiento de manera clara y concisa
   - Identifica el objetivo principal y el valor de negocio

2. **ESTRUCTURA DEL REQUERIMIENTO**
   - Actores involucrados
   - Funcionalidad principal
   - Flujo de trabajo esperado
   - Dependencias técnicas o de negocio

3. **AMBIGÜEDADES DETECTADAS**
   - Lista puntos que no están claros o pueden interpretarse de múltiples formas
   - Señala términos vagos o imprecisos

4. **INFORMACIÓN FALTANTE**
   - Criterios de aceptación incompletos
   - Casos edge no considerados
   - Requisitos no funcionales (rendimiento, seguridad, etc.)
   - Datos o contexto necesario para la implementación

5. **POSIBLES MEJORAS Y RIESGOS**
   - Sugerencias para mejorar la claridad del requerimiento
   - Riesgos técnicos o de negocio identificados
   - Consideraciones de escalabilidad, mantenibilidad y seguridad
   - Alternativas o enfoques recomendados

Proporciona un análisis detallado, profesional y accionable."""

        return prompt

    def _format_comments(self, comments: list) -> str:
        """Formatea los comentarios para el prompt."""
        if not comments:
            return "No hay comentarios"
        
        formatted = []
        for i, comment in enumerate(comments, 1):
            formatted.append(f"Comentario {i}: {comment}")
        
        return "\n".join(formatted)

    def analyze_story(self, story_data: Dict[str, Any]) -> str:
        """
        Analiza una historia de usuario usando IA.
        
        Args:
            story_data: Datos de la historia de usuario
            
        Returns:
            Análisis generado por la IA
        """
        try:
            prompt = self.create_analysis_prompt(story_data)
            
            response = completion(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"Error al analizar la historia: {str(e)}")
