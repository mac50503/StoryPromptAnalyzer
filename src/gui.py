"""Interfaz gráfica de la aplicación."""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, Menu
from typing import Optional
from dotenv import load_dotenv
import os
import sys

from src.jira_client import JiraClient
from src.ai_analyzer import AIAnalyzer
from src.settings_window import SettingsWindow
from src.i18n import I18n
from src.settings_window import SettingsWindow


class StoryAnalyzerGUI:
    """Interfaz gráfica para el analizador de historias."""

    def __init__(self, root: tk.Tk):
        """
        Inicializa la interfaz gráfica.
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        
        # Cargar variables de entorno
        load_dotenv()
        
        # Inicializar sistema de traducciones
        language = os.getenv("LANGUAGE", "en")
        self.i18n = I18n(language)
        
        self.root.title(self.i18n.get("app_title"))
        self.root.geometry("900x700")
        
        # Inicializar clientes
        self.jira_client: Optional[JiraClient] = None
        self.ai_analyzer: Optional[AIAnalyzer] = None
        
        self._setup_ui()
        self._initialize_clients()

    def _setup_ui(self) -> None:
        """Configura los elementos de la interfaz."""
        # Crear menú
        self._create_menu()
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar peso de filas y columnas
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text=self.i18n.get("app_title"), 
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, pady=(0, 20))
        
        # Frame de entrada
        input_frame = ttk.LabelFrame(main_frame, text=self.i18n.get("input_section"), padding="10")
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        # Campo de Story ID
        ttk.Label(input_frame, text=self.i18n.get("story_id_label")).grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        self.story_id_entry = ttk.Entry(input_frame, width=30)
        self.story_id_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.story_id_entry.insert(0, "PROJ-123")
        
        # Botón de análisis
        self.analyze_button = ttk.Button(
            input_frame, 
            text=self.i18n.get("analyze_button"), 
            command=self._analyze_story
        )
        self.analyze_button.grid(row=0, column=2)
        
        # Selector de proveedor
        ttk.Label(input_frame, text=self.i18n.get("provider_label")).grid(row=1, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        
        self.provider_var = tk.StringVar(value="OpenAI")
        provider_combo = ttk.Combobox(
            input_frame, 
            textvariable=self.provider_var,
            values=["OpenAI", "Anthropic"],
            state="readonly",
            width=28
        )
        provider_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))
        provider_combo.bind("<<ComboboxSelected>>", self._on_provider_change)
        
        # Selector de modelo
        ttk.Label(input_frame, text=self.i18n.get("model_label")).grid(row=2, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        
        self.model_var = tk.StringVar(value="gpt-4")
        self.model_combo = ttk.Combobox(
            input_frame, 
            textvariable=self.model_var,
            values=["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"],
            state="readonly",
            width=28
        )
        self.model_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))
        
        # Modelos por proveedor
        self.models_by_provider = {
            "OpenAI": ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"],
            "Anthropic": ["claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"]
        }
        
        # Frame de salida
        output_frame = ttk.LabelFrame(main_frame, text=self.i18n.get("analysis_section"), padding="10")
        output_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        # Área de texto con scroll
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            wrap=tk.WORD,
            width=80,
            height=30,
            font=("Consolas", 10)
        )
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Barra de estado
        self.status_var = tk.StringVar(value=self.i18n.get("status_ready"))
        status_bar = ttk.Label(
            main_frame, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        status_bar.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(10, 0))

    def _initialize_clients(self) -> None:
        """Inicializa los clientes de Jira y IA."""
        # Ya no inicializamos los clientes al inicio
        # Se inicializarán cuando el usuario presione "Analizar Historia"
        self.status_var.set(self.i18n.get("status_ready"))
    
    def _on_provider_change(self, event=None) -> None:
        """Actualiza los modelos disponibles cuando cambia el proveedor."""
        provider = self.provider_var.get()
        models = self.models_by_provider.get(provider, [])
        self.model_combo['values'] = models
        if models:
            self.model_var.set(models[0])
    
    def _get_full_model_name(self) -> str:
        """Obtiene el nombre completo del modelo con el prefijo del proveedor."""
        provider = self.provider_var.get()
        model = self.model_var.get()
        
        # LiteLLM requiere el formato: proveedor/modelo para algunos casos
        if provider == "Anthropic":
            return model  # Los modelos de Anthropic ya tienen el formato completo
        else:
            return model  # OpenAI no necesita prefijo

    def _analyze_story(self) -> None:
        """Analiza la historia de usuario ingresada."""
        story_id = self.story_id_entry.get().strip()
        
        if not story_id:
            messagebox.showwarning(
                self.i18n.get("warning"), 
                self.i18n.get("warning_empty_story")
            )
            return
        
        # Inicializar clientes si no existen
        if not self.jira_client or not self.ai_analyzer:
            try:
                self.status_var.set(self.i18n.get("status_connecting"))
                self.root.update()
                self.jira_client = JiraClient.from_env()
                self.ai_analyzer = AIAnalyzer(model=self._get_full_model_name())
            except Exception as e:
                self.status_var.set(self.i18n.get("status_error"))
                messagebox.showerror(
                    self.i18n.get("error"),
                    self.i18n.get("error_connection", error=str(e))
                )
                return
        
        # Limpiar salida anterior
        self.output_text.delete(1.0, tk.END)
        self.status_var.set(self.i18n.get("status_fetching", story_id=story_id))
        self.analyze_button.config(state="disabled")
        self.root.update()
        
        try:
            # Obtener historia de Jira
            story_data = self.jira_client.get_user_story(story_id)
            provider = self.provider_var.get()
            model = self.model_var.get()
            self.status_var.set(self.i18n.get("status_analyzing", story_id=story_id, provider=provider, model=model))
            self.root.update()
            
            # Actualizar modelo si cambió
            self.ai_analyzer.model = self._get_full_model_name()
            
            # Analizar con IA
            analysis = self.ai_analyzer.analyze_story(story_data)
            
            # Mostrar resultado
            self._display_result(story_data, analysis)
            self.status_var.set(self.i18n.get("status_completed", story_id=story_id))
            
        except Exception as e:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("error_analysis", error=str(e))
            )
            self.status_var.set(self.i18n.get("status_error"))
        finally:
            self.analyze_button.config(state="normal")

    def _display_result(self, story_data: dict, analysis: str) -> None:
        """
        Muestra el resultado del análisis.
        
        Args:
            story_data: Datos de la historia
            analysis: Análisis generado
        """
        output = f"""{'='*80}
HISTORIA DE USUARIO: {story_data['key']}
{'='*80}

Título: {story_data['title']}
Estado: {story_data['status']}
Prioridad: {story_data['priority']}

{'='*80}
ANÁLISIS GENERADO
{'='*80}

{analysis}

{'='*80}
"""
        self.output_text.insert(1.0, output)
    
    def _create_menu(self) -> None:
        """Crea la barra de menú."""
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.i18n.get("menu_file"), menu=file_menu)
        file_menu.add_command(label=self.i18n.get("menu_settings"), command=self._open_settings)
        file_menu.add_separator()
        file_menu.add_command(label=self.i18n.get("menu_exit"), command=self.root.quit)
        
        # Menú Idioma
        language_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.i18n.get("menu_language"), menu=language_menu)
        language_menu.add_radiobutton(
            label="Español", 
            command=lambda: self._change_language("es"),
            variable=tk.StringVar(value=self.i18n.language),
            value="es"
        )
        language_menu.add_radiobutton(
            label="English", 
            command=lambda: self._change_language("en"),
            variable=tk.StringVar(value=self.i18n.language),
            value="en"
        )
        
        # Menú Ayuda
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.i18n.get("menu_help"), menu=help_menu)
        help_menu.add_command(label=self.i18n.get("menu_about"), command=self._show_about)
    
    def _open_settings(self) -> None:
        """Abre la ventana de configuración."""
        SettingsWindow(self.root, self._on_settings_saved, self.i18n)
    
    def _on_settings_saved(self) -> None:
        """Callback cuando se guardan las configuraciones."""
        # Recargar variables de entorno
        load_dotenv(override=True)
        
        # Limpiar clientes para que se reinicialicen en el próximo análisis
        self.jira_client = None
        self.ai_analyzer = None
        
        self.status_var.set(self.i18n.get("status_config_saved"))
        messagebox.showinfo(
            self.i18n.get("success"), 
            self.i18n.get("success_config_saved")
        )
    
    def _change_language(self, lang_code: str) -> None:
        """
        Cambia el idioma de la aplicación.
        
        Args:
            lang_code: Código de idioma (es, en)
        """
        # Guardar en .env
        from dotenv import set_key
        
        # Crear archivo .env si no existe
        if not os.path.exists(".env"):
            with open(".env", 'w') as f:
                f.write("")
        
        set_key(".env", "LANGUAGE", lang_code)
        
        # Recargar variables de entorno
        load_dotenv(override=True)
        
        # Actualizar idioma
        self.i18n.set_language(lang_code)
        
        # Mostrar mensaje de confirmación
        messagebox.showinfo(
            self.i18n.get("success"),
            self.i18n.get("language_changed")
        )
        
        # Sugerir reiniciar para aplicar completamente
        if messagebox.askyesno(
            self.i18n.get("restart_title"),
            self.i18n.get("restart_message")
        ):
            # Reiniciar la aplicación
            self.root.destroy()
            python = sys.executable
            os.execl(python, python, *sys.argv)
    
    def _show_about(self) -> None:
        """Muestra información sobre la aplicación."""
        messagebox.showinfo(
            self.i18n.get("menu_about"),
            self.i18n.get("about_text")
        )


def main() -> None:
    """Función principal para ejecutar la aplicación."""
    root = tk.Tk()
    app = StoryAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
