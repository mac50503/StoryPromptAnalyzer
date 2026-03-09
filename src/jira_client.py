"""Cliente para conectarse a Jira y obtener historias de usuario."""

from typing import Dict, Any, Optional
from jira import JIRA
import os


class JiraClient:
    """Cliente para interactuar con Jira."""

    def __init__(self, url: str, email: str, api_token: str):
        """
        Inicializa el cliente de Jira.
        
        Args:
            url: URL del servidor de Jira
            email: Email del usuario
            api_token: Token de API de Jira
        """
        self.jira = JIRA(server=url, basic_auth=(email, api_token))

    @classmethod
    def from_env(cls) -> "JiraClient":
        """Crea un cliente desde variables de entorno."""
        url = os.getenv("JIRA_URL", "")
        email = os.getenv("JIRA_EMAIL", "")
        token = os.getenv("JIRA_API_TOKEN", "")
        
        if not all([url, email, token]):
            raise ValueError("Faltan credenciales de Jira en el archivo .env")
        
        return cls(url, email, token)

    def get_user_story(self, story_key: str) -> Dict[str, Any]:
        """
        Obtiene una historia de usuario de Jira.
        
        Args:
            story_key: Clave de la historia (ej: PROJ-123)
            
        Returns:
            Diccionario con los datos de la historia
        """
        try:
            issue = self.jira.issue(story_key)
            
            # Extraer criterios de aceptación (pueden estar en diferentes campos)
            acceptance_criteria = ""
            if hasattr(issue.fields, 'customfield_10000'):
                acceptance_criteria = getattr(issue.fields, 'customfield_10000', "")
            
            # Obtener comentarios
            comments = [comment.body for comment in issue.fields.comment.comments]
            
            # Obtener etiquetas
            labels = issue.fields.labels if hasattr(issue.fields, 'labels') else []
            
            return {
                "key": issue.key,
                "title": issue.fields.summary,
                "description": issue.fields.description or "",
                "acceptance_criteria": acceptance_criteria or "",
                "comments": comments,
                "labels": labels,
                "status": issue.fields.status.name,
                "priority": issue.fields.priority.name if issue.fields.priority else "N/A"
            }
        except Exception as e:
            raise Exception(f"Error al obtener la historia {story_key}: {str(e)}")
