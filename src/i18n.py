"""Sistema de internacionalización para la aplicación."""

import os
from typing import Dict


class I18n:
    """Gestor de traducciones."""
    
    TRANSLATIONS: Dict[str, Dict[str, str]] = {
        "es": {
            # Ventana principal
            "app_title": "Story Prompt Analyzer",
            "input_section": "Entrada",
            "story_id_label": "Story ID:",
            "provider_label": "Proveedor:",
            "model_label": "Modelo:",
            "analyze_button": "Analizar Historia",
            "analysis_section": "Análisis",
            "status_ready": "Listo - Configure las credenciales en Archivo → Configuración",
            "status_connecting": "Conectando a Jira...",
            "status_fetching": "Obteniendo historia {story_id}...",
            "status_analyzing": "Analizando historia {story_id} con {provider} - {model}...",
            "status_completed": "Análisis completado para {story_id}",
            "status_error": "Error en el análisis",
            "status_config_saved": "Configuración guardada - Lista para usar",
            
            # Menú
            "menu_file": "Archivo",
            "menu_settings": "Configuración",
            "menu_exit": "Salir",
            "menu_language": "Idioma",
            "menu_help": "Ayuda",
            "menu_about": "Acerca de",
            
            # Mensajes
            "warning": "Advertencia",
            "error": "Error",
            "success": "Éxito",
            "warning_empty_story": "Por favor ingresa un Story ID",
            "error_connection": "No se pudo conectar a Jira:\n\n{error}\n\nVerifica tu configuración en Archivo → Configuración",
            "error_analysis": "Error al analizar la historia:\n\n{error}",
            "success_config_saved": "Configuración guardada correctamente",
            "about_text": "Story Prompt Analyzer v1.0\n\nAnaliza historias de usuario de Jira usando IA\n\nSoporta OpenAI y Anthropic",
            "language_changed": "Idioma cambiado correctamente",
            "restart_title": "Reiniciar aplicación",
            "restart_message": "Para aplicar completamente el cambio de idioma, se recomienda reiniciar la aplicación.\n\n¿Desea reiniciar ahora?",
            
            # Ventana de configuración
            "settings_title": "Configuración",
            "settings_header": "Configuración de la Aplicación",
            "jira_section": "Configuración de Jira",
            "jira_url": "JIRA URL:",
            "jira_email": "JIRA Email:",
            "jira_token": "JIRA API Token:",
            "openai_section": "Configuración de OpenAI",
            "openai_key": "OpenAI API Key:",
            "anthropic_section": "Configuración de Anthropic",
            "anthropic_key": "Anthropic API Key:",
            "general_section": "Configuración General",
            "default_model": "Modelo por Defecto:",
            "language": "Idioma:",
            "button_cancel": "Cancelar",
            "button_save": "Guardar",
            "button_apply": "Aplicar",
            "error_save_config": "Error al guardar la configuración:\n\n{error}",
        },
        "en": {
            # Main window
            "app_title": "Story Prompt Analyzer",
            "input_section": "Input",
            "story_id_label": "Story ID:",
            "provider_label": "Provider:",
            "model_label": "Model:",
            "analyze_button": "Analyze Story",
            "analysis_section": "Analysis",
            "status_ready": "Ready - Configure credentials in File → Settings",
            "status_connecting": "Connecting to Jira...",
            "status_fetching": "Fetching story {story_id}...",
            "status_analyzing": "Analyzing story {story_id} with {provider} - {model}...",
            "status_completed": "Analysis completed for {story_id}",
            "status_error": "Analysis error",
            "status_config_saved": "Configuration saved - Ready to use",
            
            # Menu
            "menu_file": "File",
            "menu_settings": "Settings",
            "menu_exit": "Exit",
            "menu_language": "Language",
            "menu_help": "Help",
            "menu_about": "About",
            
            # Messages
            "warning": "Warning",
            "error": "Error",
            "success": "Success",
            "warning_empty_story": "Please enter a Story ID",
            "error_connection": "Could not connect to Jira:\n\n{error}\n\nCheck your configuration in File → Settings",
            "error_analysis": "Error analyzing story:\n\n{error}",
            "success_config_saved": "Configuration saved successfully",
            "about_text": "Story Prompt Analyzer v1.0\n\nAnalyzes Jira user stories using AI\n\nSupports OpenAI and Anthropic",
            "language_changed": "Language changed successfully",
            "restart_title": "Restart application",
            "restart_message": "To fully apply the language change, it is recommended to restart the application.\n\nDo you want to restart now?",
            
            # Settings window
            "settings_title": "Settings",
            "settings_header": "Application Settings",
            "jira_section": "Jira Configuration",
            "jira_url": "JIRA URL:",
            "jira_email": "JIRA Email:",
            "jira_token": "JIRA API Token:",
            "openai_section": "OpenAI Configuration",
            "openai_key": "OpenAI API Key:",
            "anthropic_section": "Anthropic Configuration",
            "anthropic_key": "Anthropic API Key:",
            "general_section": "General Settings",
            "default_model": "Default Model:",
            "language": "Language:",
            "button_cancel": "Cancel",
            "button_save": "Save",
            "button_apply": "Apply",
            "error_save_config": "Error saving configuration:\n\n{error}",
        }
    }
    
    def __init__(self, language: str = "en"):
        """
        Inicializa el gestor de traducciones.
        
        Args:
            language: Código de idioma (es, en)
        """
        self.language = language if language in self.TRANSLATIONS else "en"
    
    def get(self, key: str, **kwargs) -> str:
        """
        Obtiene una traducción.
        
        Args:
            key: Clave de la traducción
            **kwargs: Parámetros para formatear el texto
            
        Returns:
            Texto traducido
        """
        text = self.TRANSLATIONS.get(self.language, {}).get(key, key)
        if kwargs:
            return text.format(**kwargs)
        return text
    
    def set_language(self, language: str) -> None:
        """
        Cambia el idioma.
        
        Args:
            language: Código de idioma (es, en)
        """
        if language in self.TRANSLATIONS:
            self.language = language
    
    @staticmethod
    def get_available_languages() -> Dict[str, str]:
        """Retorna los idiomas disponibles."""
        return {
            "es": "Español",
            "en": "English"
        }
