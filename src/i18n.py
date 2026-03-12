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
            "story_ids_label": "Story IDs (separados por coma o línea):",
            "include_children_label": "Incluir child issues (subtareas/historias hijas)",
            "provider_label": "Proveedor:",
            "model_label": "Modelo:",
            "template_label": "Enfoque de Análisis:",
            "user_notes_label": "Notas/Contexto:",
            "analysis_mode_label": "Modo de Análisis:",
            "analysis_mode_standard": "Estándar",
            "analysis_mode_blaze": "Blaze Rules Context",
            "analyze_button": "Analizar Historia",
            "analyze_sprint_button": "Analizar Sprint",
            "generate_tests_button": "Generar Test Cases",
            "fetch_button": "Obtener de Jira",
            "export_button": "Exportar",
            "analysis_section": "Análisis",
            "followup_section": "Hacer Preguntas de Seguimiento",
            "send_button": "Enviar",
            "tab_single": "Historia Individual",
            "tab_sprint": "Análisis de Sprint",
            
            # Templates
            "template_standard": "Estándar (Balanceado)",
            "template_security": "Seguridad",
            "template_performance": "Rendimiento",
            "template_api": "Diseño de API",
            "template_database": "Base de Datos",
            "status_ready": "Listo - Configure las credenciales en Archivo → Configuración",
            "status_connecting": "Conectando a Jira...",
            "status_fetching": "Obteniendo historia {story_id}...",
            "status_fetched": "Historia {story_id} obtenida - Revisa y luego analiza",
            "status_fetching_children": "Obteniendo child issues...",
            "status_fetching_multiple": "Obteniendo {count} historias de Jira...",
            "status_analyzing": "Analizando historia {story_id} con {provider} - {model}...",
            "status_analyzing_sprint": "Analizando sprint con {count} historias...",
            "status_generating_plan": "Generando plan de trabajo y dependencias...",
            "status_generating_tests": "Generando test cases...",
            "status_completed": "Análisis completado para {story_id}",
            "status_completed_sprint": "Análisis de sprint completado ({count} historias)",
            "status_error": "Error en el análisis",
            "status_config_saved": "Configuración guardada - Lista para usar",
            "status_processing": "Procesando tu pregunta...",
            "status_exported": "Análisis exportado a {filename}",
            
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
            "warning_empty_stories": "Por favor ingresa al menos un Story ID",
            "warning_no_analysis": "Por favor analiza una historia primero antes de hacer preguntas de seguimiento",
            "warning_empty_analysis": "No hay contenido para exportar",
            "error_connection": "No se pudo conectar a Jira:\n\n{error}\n\nVerifica tu configuración en Archivo → Configuración",
            "error_analysis": "Error al analizar la historia:\n\n{error}",
            "error_followup": "Error al procesar pregunta de seguimiento:\n\n{error}",
            "error_export": "Error al exportar el análisis:\n\n{error}",
            "success_config_saved": "Configuración guardada correctamente",
            "export_success": "Análisis exportado exitosamente a {filename}",
            "export_title": "Exportar Análisis",
            "text_files": "Archivos de texto",
            "markdown_files": "Archivos Markdown",
            "word_files": "Archivos Word",
            "pdf_files": "Archivos PDF",
            "all_files": "Todos los archivos",
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
            
            # Jira comment posting
            "post_to_jira_button": "Publicar en Jira",
            "edit_comment_title": "Editar Comentario para Jira",
            "comment_preview_label": "Vista previa del comentario (editable):",
            "post_comment_button": "Publicar Comentario",
            "cancel_button": "Cancelar",
            "status_posting_comment": "Publicando comentario en {story_id}...",
            "status_comment_posted": "Comentario publicado exitosamente en {story_id}",
            "error_post_comment": "Error al publicar comentario:\n\n{error}",
            "confirm_post_title": "Confirmar Publicación",
            "confirm_post_message": "¿Estás seguro de que deseas publicar este comentario en {story_id}?",
        },
        "en": {
            # Main window
            "app_title": "Story Prompt Analyzer",
            "input_section": "Input",
            "story_id_label": "Story ID:",
            "story_ids_label": "Story IDs (comma or line separated):",
            "include_children_label": "Include child issues (subtasks/child stories)",
            "provider_label": "Provider:",
            "model_label": "Model:",
            "template_label": "Analysis Focus:",
            "user_notes_label": "Notes/Context:",
            "analysis_mode_label": "Analysis Mode:",
            "analysis_mode_standard": "Standard",
            "analysis_mode_blaze": "Blaze Rules Context",
            "analyze_button": "Analyze Story",
            "analyze_sprint_button": "Analyze Sprint",
            "generate_tests_button": "Generate Test Cases",
            "fetch_button": "Fetch from Jira",
            "export_button": "Export",
            "analysis_section": "Analysis",
            "followup_section": "Ask Follow-up Questions",
            "send_button": "Send",
            "tab_single": "Single Story",
            "tab_sprint": "Sprint Analysis",
            
            # Templates
            "template_standard": "Standard (Balanced)",
            "template_security": "Security Focus",
            "template_performance": "Performance Focus",
            "template_api": "API Design",
            "template_database": "Database Focus",
            "status_ready": "Ready - Configure credentials in File → Settings",
            "status_connecting": "Connecting to Jira...",
            "status_fetching": "Fetching story {story_id}...",
            "status_fetched": "Story {story_id} fetched - Review and then analyze",
            "status_fetching_children": "Fetching child issues...",
            "status_fetching_multiple": "Fetching {count} stories from Jira...",
            "status_analyzing": "Analyzing story {story_id} with {provider} - {model}...",
            "status_analyzing_sprint": "Analyzing sprint with {count} stories...",
            "status_generating_plan": "Generating work plan and dependencies...",
            "status_generating_tests": "Generating test cases...",
            "status_completed": "Analysis completed for {story_id}",
            "status_completed_sprint": "Sprint analysis completed ({count} stories)",
            "status_error": "Analysis error",
            "status_config_saved": "Configuration saved - Ready to use",
            "status_processing": "Processing your question...",
            "status_exported": "Analysis exported to {filename}",
            
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
            "warning_empty_stories": "Please enter at least one Story ID",
            "warning_no_analysis": "Please analyze a story first before asking follow-up questions",
            "warning_empty_analysis": "No content to export",
            "error_connection": "Could not connect to Jira:\n\n{error}\n\nCheck your configuration in File → Settings",
            "error_analysis": "Error analyzing story:\n\n{error}",
            "error_followup": "Error processing follow-up question:\n\n{error}",
            "error_export": "Error exporting analysis:\n\n{error}",
            "success_config_saved": "Configuration saved successfully",
            "export_success": "Analysis exported successfully to {filename}",
            "export_title": "Export Analysis",
            "text_files": "Text files",
            "markdown_files": "Markdown files",
            "word_files": "Word files",
            "pdf_files": "PDF files",
            "all_files": "All files",
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
            
            # Jira comment posting
            "post_to_jira_button": "Post to Jira",
            "edit_comment_title": "Edit Comment for Jira",
            "comment_preview_label": "Comment preview (editable):",
            "post_comment_button": "Post Comment",
            "cancel_button": "Cancel",
            "status_posting_comment": "Posting comment to {story_id}...",
            "status_comment_posted": "Comment posted successfully to {story_id}",
            "error_post_comment": "Error posting comment:\n\n{error}",
            "confirm_post_title": "Confirm Post",
            "confirm_post_message": "Are you sure you want to post this comment to {story_id}?",
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
