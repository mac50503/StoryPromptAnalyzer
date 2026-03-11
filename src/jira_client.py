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
            
            # Obtener campos configurados por el usuario (puede ser una lista separada por comas)
            user_fields = os.getenv("JIRA_ACCEPTANCE_CRITERIA_FIELD", "")
            if user_fields:
                # Separar por comas y limpiar espacios
                fields_list = [f.strip() for f in user_fields.split(',') if f.strip()]
                
                # Intentar con cada campo configurado
                for field in fields_list:
                    if hasattr(issue.fields, field):
                        value = getattr(issue.fields, field, None)
                        if value:
                            acceptance_criteria = str(value)
                            break
            
            # Si no se encontró, buscar en campos comunes
            if not acceptance_criteria:
                # Lista de campos comunes donde pueden estar los criterios de aceptación
                possible_fields = [
                    'customfield_10054',  # Campo común
                    'customfield_10000',  # Campo común en Jira Cloud
                    'customfield_10100',
                    'customfield_10200',
                    'customfield_12000',
                    'customfield_10007',  # Otro campo común
                    'customfield_10008',
                    'customfield_10009',
                    'customfield_10010',
                ]
                
                # Intentar encontrar criterios de aceptación en los campos custom
                for field in possible_fields:
                    if hasattr(issue.fields, field):
                        value = getattr(issue.fields, field, None)
                        if value:
                            # Convertir a string sin límite de caracteres
                            acceptance_criteria = str(value)
                            break
            
            # Si no se encontró en custom fields, buscar en la descripción
            # A veces los criterios están al final de la descripción
            if not acceptance_criteria and issue.fields.description:
                desc = issue.fields.description
                # Buscar secciones comunes de criterios de aceptación
                markers = [
                    'Acceptance Criteria',
                    'Criterios de Aceptación',
                    'AC:',
                    'Acceptance:',
                    'Criteria:',
                ]
                for marker in markers:
                    if marker in desc:
                        # Extraer desde el marcador hasta el final
                        parts = desc.split(marker, 1)
                        if len(parts) > 1:
                            acceptance_criteria = parts[1].strip()
                            break
            
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
    
    def get_all_fields(self, story_key: str) -> Dict[str, Any]:
        """
        Obtiene todos los campos disponibles de una historia para debugging.
        Útil para encontrar el campo correcto de acceptance criteria.
        
        Args:
            story_key: Clave de la historia (ej: PROJ-123)
            
        Returns:
            Diccionario con campos agrupados por tipo (con contenido, vacíos, system)
        """
        try:
            issue = self.jira.issue(story_key)
            
            # Agrupar campos
            fields_with_content = {}
            empty_fields = []
            system_fields = []
            
            for field_name in dir(issue.fields):
                if field_name.startswith('_'):
                    continue
                    
                try:
                    value = getattr(issue.fields, field_name)
                    
                    # Clasificar campos del sistema
                    if field_name in ['summary', 'description', 'status', 'priority', 'issuetype', 
                                     'project', 'created', 'updated', 'reporter', 'assignee',
                                     'labels', 'components', 'fixVersions', 'versions', 'comment']:
                        system_fields.append(field_name)
                        continue
                    
                    # Campos con contenido
                    if value is not None and value != "" and value != []:
                        str_value = str(value)
                        if len(str_value) > 500:
                            fields_with_content[field_name] = str_value[:500] + f"... [TRUNCATED - Total: {len(str_value)} chars]"
                        else:
                            fields_with_content[field_name] = str_value
                    else:
                        # Campos vacíos
                        empty_fields.append(field_name)
                        
                except:
                    pass
            
            return {
                'with_content': fields_with_content,
                'empty': empty_fields,
                'system': system_fields
            }
        except Exception as e:
            raise Exception(f"Error getting fields for {story_key}: {str(e)}")
    
    def post_comment(self, story_key: str, comment_text: str) -> bool:
        """
        Publica un comentario en una historia de Jira.
        
        Args:
            story_key: Clave de la historia (ej: PROJ-123)
            comment_text: Texto del comentario a publicar
            
        Returns:
            True si se publicó exitosamente, False en caso contrario
        """
        try:
            self.jira.add_comment(story_key, comment_text)
            return True
        except Exception as e:
            raise Exception(f"Error posting comment to {story_key}: {str(e)}")
    
    def get_child_issues(self, parent_key: str) -> list[str]:
        """
        Obtiene todos los child issues (subtareas, historias hijas) de un issue padre.
        Útil para analizar un Epic completo con todas sus historias.
        
        Args:
            parent_key: Clave del issue padre (ej: EPIC-123)
            
        Returns:
            Lista de claves de los child issues (ej: ['PROJ-123', 'PROJ-124'])
        """
        try:
            parent_issue = self.jira.issue(parent_key)
            child_keys = []
            
            # Obtener subtasks (subtareas directas)
            if hasattr(parent_issue.fields, 'subtasks') and parent_issue.fields.subtasks:
                for subtask in parent_issue.fields.subtasks:
                    child_keys.append(subtask.key)
            
            # Obtener issues que tienen este como parent (para Epics)
            # Buscar usando JQL: parent = EPIC-123
            try:
                jql = f'parent = {parent_key}'
                child_issues = self.jira.search_issues(jql, maxResults=100)
                for issue in child_issues:
                    if issue.key not in child_keys:
                        child_keys.append(issue.key)
            except:
                pass
            
            # También buscar por Epic Link (campo común en Jira)
            try:
                # Intentar con diferentes campos de Epic Link
                epic_link_fields = ['customfield_10014', 'customfield_10008', 'customfield_10100']
                for field in epic_link_fields:
                    try:
                        jql = f'"{field}" = {parent_key}'
                        epic_issues = self.jira.search_issues(jql, maxResults=100)
                        for issue in epic_issues:
                            if issue.key not in child_keys:
                                child_keys.append(issue.key)
                        break  # Si funciona, no intentar otros campos
                    except:
                        continue
            except:
                pass
            
            return child_keys
            
        except Exception as e:
            raise Exception(f"Error getting child issues for {parent_key}: {str(e)}")

