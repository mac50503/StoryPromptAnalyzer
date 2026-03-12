"""Interfaz gráfica de la aplicación."""

import tkinter as tk
from tkinter import ttk, messagebox, Menu, filedialog
from typing import Optional
from dotenv import load_dotenv
import os
import sys
from datetime import datetime

from src.jira_client import JiraClient
from src.ai_analyzer import AIAnalyzer
from src.settings_window import SettingsWindow
from src.i18n import I18n
from src.rich_text_viewer import RichTextViewer
from src.export_utils import ExportManager


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
        
        # Configurar el protocolo de cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        
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
        main_frame.rowconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(
            main_frame, 
            text=self.i18n.get("app_title"), 
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, pady=(0, 20))
        
        # Crear notebook (tabs)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tab 1: Single Story Analysis
        self.single_tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.single_tab, text=self.i18n.get("tab_single"))
        
        # Tab 2: Sprint Analysis
        self.sprint_tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.sprint_tab, text=self.i18n.get("tab_sprint"))
        
        # Setup each tab
        self._setup_single_story_tab()
        self._setup_sprint_analysis_tab()
        
        # Barra de estado (compartida)
        self.status_var = tk.StringVar(value=self.i18n.get("status_ready"))
        status_bar = ttk.Label(
            main_frame, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        status_bar.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def _setup_single_story_tab(self) -> None:
        """Configura el tab de análisis de historia individual."""
        # Configurar peso de filas y columnas
        self.single_tab.columnconfigure(0, weight=1)
        self.single_tab.rowconfigure(1, weight=1)
        
        # Frame de entrada
        input_frame = ttk.LabelFrame(self.single_tab, text=self.i18n.get("input_section"), padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        
        # Campo de Story ID
        ttk.Label(input_frame, text=self.i18n.get("story_id_label")).grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        self.story_id_entry = ttk.Entry(input_frame, width=30)
        self.story_id_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.story_id_entry.insert(0, "PROJ-123")
        
        # Botón de fetch
        self.fetch_button = ttk.Button(
            input_frame, 
            text=self.i18n.get("fetch_button"), 
            command=self._fetch_story
        )
        self.fetch_button.grid(row=0, column=2, padx=(0, 5))
        
        # Botón de debug (pequeño, para ver campos de Jira)
        self.debug_button = ttk.Button(
            input_frame, 
            text="🔍", 
            command=self._debug_jira_fields,
            width=3
        )
        self.debug_button.grid(row=0, column=3, padx=(0, 5))
        
        # Botón de análisis
        self.analyze_button = ttk.Button(
            input_frame, 
            text=self.i18n.get("analyze_button"), 
            command=self._analyze_story
        )
        self.analyze_button.grid(row=0, column=4, padx=(0, 5))
        
        # Botón de generar test cases
        self.generate_tests_button = ttk.Button(
            input_frame,
            text=self.i18n.get("generate_tests_button"),
            command=self._generate_test_cases,
            state="disabled"
        )
        self.generate_tests_button.grid(row=0, column=5, padx=(0, 5))
        
        # Botón de exportar
        self.export_button = ttk.Button(
            input_frame,
            text=self.i18n.get("export_button"),
            command=self._export_analysis,
            state="disabled"
        )
        self.export_button.grid(row=0, column=6, padx=(0, 5))
        
        # Botón de publicar en Jira
        self.post_to_jira_button = ttk.Button(
            input_frame,
            text=self.i18n.get("post_to_jira_button"),
            command=self._open_post_to_jira_dialog,
            state="disabled"
        )
        self.post_to_jira_button.grid(row=0, column=7)
        
        # Botón de copiar prompt para Kiro (solo visible en modo Blaze)
        self.copy_kiro_prompt_button = ttk.Button(
            input_frame,
            text="📋 Copy Kiro Prompt",
            command=self._copy_kiro_prompt,
            state="disabled"
        )
        self.copy_kiro_prompt_button.grid(row=0, column=8, padx=(5, 0))
        self.copy_kiro_prompt_button.grid_remove()  # Ocultar por defecto
        
        # Variable para guardar el último prompt de Kiro generado
        self.last_kiro_prompt = None
        
        # Selector de proveedor
        ttk.Label(input_frame, text=self.i18n.get("provider_label")).grid(row=1, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        
        self.provider_var = tk.StringVar(value="OpenAI")
        provider_combo = ttk.Combobox(
            input_frame, 
            textvariable=self.provider_var,
            values=["OpenAI", "Anthropic", "Groq (Free)"],
            state="readonly",
            width=28
        )
        provider_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))
        provider_combo.bind("<<ComboboxSelected>>", self._on_provider_change)
        
        # Selector de modelo
        ttk.Label(input_frame, text=self.i18n.get("model_label")).grid(row=2, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        
        # Modelos por proveedor
        self.models_by_provider = {
            "OpenAI": ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"],
            "Anthropic": ["claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"],
            "Groq (Free)": ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"]
        }
        
        # Obtener modelo por defecto del .env
        default_model = os.getenv("AI_MODEL", "gpt-4-turbo")
        
        self.model_var = tk.StringVar(value=default_model)
        self.model_combo = ttk.Combobox(
            input_frame, 
            textvariable=self.model_var,
            values=self.models_by_provider["OpenAI"],
            state="readonly",
            width=28
        )
        self.model_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))
        
        # Campo de notas del usuario
        ttk.Label(input_frame, text=self.i18n.get("user_notes_label")).grid(row=3, column=0, sticky=(tk.W, tk.N), padx=(0, 10), pady=(10, 0))
        
        self.user_notes_text = tk.Text(
            input_frame,
            width=30,
            height=3,
            font=("Segoe UI", 9),
            wrap=tk.WORD
        )
        self.user_notes_text.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))
        
        # Analysis mode selection
        ttk.Label(input_frame, text=self.i18n.get("analysis_mode_label")).grid(row=4, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        
        self.analysis_mode_var = tk.StringVar(value="standard")
        mode_frame = ttk.Frame(input_frame)
        mode_frame.grid(row=4, column=1, columnspan=2, sticky=tk.W, pady=(10, 0))
        
        ttk.Radiobutton(
            mode_frame,
            text=self.i18n.get("analysis_mode_standard"),
            variable=self.analysis_mode_var,
            value="standard"
        ).pack(side=tk.LEFT, padx=(0, 15))
        
        ttk.Radiobutton(
            mode_frame,
            text=self.i18n.get("analysis_mode_blaze"),
            variable=self.analysis_mode_var,
            value="blaze"
        ).pack(side=tk.LEFT)
        
        # Frame de salida
        output_frame = ttk.LabelFrame(self.single_tab, text=self.i18n.get("analysis_section"), padding="10")
        output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        # Área de texto enriquecido con scroll
        self.output_text = RichTextViewer(
            output_frame,
            width=80,
            height=20,
            font=("Consolas", 10),
            bg='white',
            fg='#2c3e50'
        )
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Frame de seguimiento/chat
        followup_frame = ttk.LabelFrame(self.single_tab, text=self.i18n.get("followup_section"), padding="10")
        followup_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        followup_frame.columnconfigure(0, weight=1)
        
        # Campo de entrada para preguntas de seguimiento
        self.followup_entry = ttk.Entry(followup_frame, width=80)
        self.followup_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        self.followup_entry.bind("<Return>", lambda e: self._send_followup())
        
        # Botón de enviar
        self.followup_button = ttk.Button(
            followup_frame,
            text=self.i18n.get("send_button"),
            command=self._send_followup,
            state="disabled"
        )
        self.followup_button.grid(row=0, column=1)
        
        # Variable para mantener el historial de conversación
        self.conversation_history = []
        self.current_story_data = None
        
    def _setup_sprint_analysis_tab(self) -> None:
        """Configura el tab de análisis de sprint."""
        # Configurar peso de filas y columnas
        self.sprint_tab.columnconfigure(0, weight=1)
        self.sprint_tab.rowconfigure(1, weight=1)
        
        # Frame de entrada
        sprint_input_frame = ttk.LabelFrame(self.sprint_tab, text=self.i18n.get("input_section"), padding="10")
        sprint_input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        sprint_input_frame.columnconfigure(1, weight=1)
        
        # Campo de Story IDs
        ttk.Label(sprint_input_frame, text=self.i18n.get("story_ids_label")).grid(row=0, column=0, sticky=(tk.W, tk.N), padx=(0, 10))
        
        self.story_ids_text = tk.Text(
            sprint_input_frame,
            width=40,
            height=5,
            font=("Segoe UI", 9),
            wrap=tk.WORD
        )
        self.story_ids_text.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        self.story_ids_text.insert("1.0", "PROJ-123, PROJ-124, PROJ-125")
        
        # Checkbox para incluir child issues
        self.include_children_var = tk.BooleanVar(value=False)
        self.include_children_check = ttk.Checkbutton(
            sprint_input_frame,
            text=self.i18n.get("include_children_label"),
            variable=self.include_children_var
        )
        self.include_children_check.grid(row=1, column=1, sticky=tk.W, pady=(5, 0))
        
        # Botón de análisis de sprint
        self.analyze_sprint_button = ttk.Button(
            sprint_input_frame, 
            text=self.i18n.get("analyze_sprint_button"), 
            command=self._analyze_sprint
        )
        self.analyze_sprint_button.grid(row=0, column=2, padx=(0, 5), sticky=tk.N)
        
        # Botón de exportar sprint
        self.export_sprint_button = ttk.Button(
            sprint_input_frame,
            text=self.i18n.get("export_button"),
            command=self._export_sprint_analysis,
            state="disabled"
        )
        self.export_sprint_button.grid(row=0, column=3, sticky=tk.N)
        
        # Selector de proveedor
        ttk.Label(sprint_input_frame, text=self.i18n.get("provider_label")).grid(row=2, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        
        # Usar las mismas variables que el tab single story
        sprint_provider_combo = ttk.Combobox(
            sprint_input_frame, 
            textvariable=self.provider_var,
            values=["OpenAI", "Anthropic", "Groq (Free)"],
            state="readonly",
            width=28
        )
        sprint_provider_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))
        sprint_provider_combo.bind("<<ComboboxSelected>>", self._on_provider_change)
        
        # Selector de modelo
        ttk.Label(sprint_input_frame, text=self.i18n.get("model_label")).grid(row=3, column=0, sticky=tk.W, padx=(0, 10), pady=(10, 0))
        
        self.sprint_model_combo = ttk.Combobox(
            sprint_input_frame, 
            textvariable=self.model_var,
            values=self.models_by_provider["OpenAI"],
            state="readonly",
            width=28
        )
        self.sprint_model_combo.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))
        
        # Frame de salida
        sprint_output_frame = ttk.LabelFrame(self.sprint_tab, text=self.i18n.get("analysis_section"), padding="10")
        sprint_output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        sprint_output_frame.columnconfigure(0, weight=1)
        sprint_output_frame.rowconfigure(0, weight=1)
        
        # Área de texto para análisis de sprint
        self.sprint_output_text = RichTextViewer(
            sprint_output_frame,
            width=80,
            height=25,
            font=("Consolas", 10),
            bg='white',
            fg='#2c3e50'
        )
        self.sprint_output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Variable para mantener datos del sprint
        self.current_sprint_data = None

    def _initialize_clients(self) -> None:
        """Inicializa los clientes de Jira y IA."""
        # Ya no inicializamos los clientes al inicio
        # Se inicializarán cuando el usuario presione "Analizar Historia"
        self.status_var.set(self.i18n.get("status_ready"))
    
    def _on_closing(self) -> None:
        """Maneja el cierre de la ventana correctamente."""
        try:
            # Destruir la ventana y terminar el proceso
            self.root.quit()
            self.root.destroy()
        except:
            pass
        finally:
            # Asegurar que el proceso termine
            sys.exit(0)
    
    def _fetch_story(self) -> None:
        """Obtiene y muestra la información de Jira sin analizar."""
        story_id = self.story_id_entry.get().strip()
        
        if not story_id:
            messagebox.showwarning(
                self.i18n.get("warning"), 
                self.i18n.get("warning_empty_story")
            )
            return
        
        # Inicializar cliente de Jira si no existe
        if not self.jira_client:
            try:
                self.status_var.set(self.i18n.get("status_connecting"))
                self.root.update()
                self.jira_client = JiraClient.from_env()
            except Exception as e:
                self.status_var.set(self.i18n.get("status_error"))
                messagebox.showerror(
                    self.i18n.get("error"),
                    self.i18n.get("error_connection", error=str(e))
                )
                return
        
        # Limpiar salida anterior
        self.output_text.clear()
        self.conversation_history = []
        self.current_story_data = None
        self.followup_button.config(state="disabled")
        self.export_button.config(state="disabled")
        self.post_to_jira_button.config(state="disabled")
        self.generate_tests_button.config(state="disabled")
        
        self.status_var.set(self.i18n.get("status_fetching", story_id=story_id))
        self.fetch_button.config(state="disabled")
        self.root.update()
        
        try:
            # Obtener notas del usuario
            user_notes = self.user_notes_text.get("1.0", tk.END).strip()
            
            # Obtener historia de Jira
            story_data = self.jira_client.get_user_story(story_id)
            
            # Agregar notas del usuario al story_data si existen
            if user_notes:
                story_data['user_notes'] = user_notes
            
            self.current_story_data = story_data
            
            # Mostrar información de la historia
            self._display_story_info(story_data)
            
            self.status_var.set(self.i18n.get("status_fetched", story_id=story_id))
            
        except Exception as e:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("error_analysis", error=str(e))
            )
            self.status_var.set(self.i18n.get("status_error"))
        finally:
            self.fetch_button.config(state="normal")
    
    def _display_story_info(self, story_data: dict) -> None:
        """
        Muestra la información de la historia obtenida de Jira.
        
        Args:
            story_data: Datos de la historia
        """
        info = f"""{'='*80}
JIRA STORY INFORMATION
{'='*80}

Story ID: {story_data['key']}
Title: {story_data['title']}
Status: {story_data['status']}
Priority: {story_data['priority']}
Labels: {', '.join(story_data['labels']) if story_data['labels'] else 'None'}

{'='*80}
DESCRIPTION
{'='*80}

{story_data['description'] or 'No description provided'}

{'='*80}
ACCEPTANCE CRITERIA
{'='*80}

{story_data['acceptance_criteria'] or 'No acceptance criteria specified'}

{'='*80}
COMMENTS ({len(story_data['comments'])})
{'='*80}

"""
        if story_data['comments']:
            for i, comment in enumerate(story_data['comments'], 1):
                info += f"Comment {i}:\n{comment}\n\n"
        else:
            info += "No comments\n\n"
        
        if story_data.get('user_notes'):
            info += f"""{'='*80}
USER NOTES/CONTEXT
{'='*80}

{story_data['user_notes']}

"""
        
        info += f"""{'='*80}

Ready to analyze! Click "Analyze Story" to generate AI analysis.

{'='*80}
"""
        
        self.output_text.append_text(info, 'normal')
    
    def _debug_jira_fields(self) -> None:
        """Muestra todos los campos de Jira para debugging."""
        story_id = self.story_id_entry.get().strip()
        
        if not story_id:
            messagebox.showwarning(
                "Debug", 
                "Please enter a Story ID first"
            )
            return
        
        # Inicializar cliente de Jira si no existe
        if not self.jira_client:
            try:
                self.jira_client = JiraClient.from_env()
            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Could not connect to Jira:\n\n{str(e)}"
                )
                return
        
        try:
            all_fields = self.jira_client.get_all_fields(story_id)
            
            # Mostrar en una ventana de diálogo
            debug_window = tk.Toplevel(self.root)
            debug_window.title(f"Jira Fields Debug - {story_id}")
            debug_window.geometry("900x700")
            
            # Frame con scroll
            frame = ttk.Frame(debug_window, padding="10")
            frame.pack(fill=tk.BOTH, expand=True)
            
            # Text widget con scroll
            text_widget = tk.Text(frame, wrap=tk.WORD, font=("Courier", 9))
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_widget.yview)
            text_widget.configure(yscrollcommand=scrollbar.set)
            
            text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Agregar información
            text_widget.insert("1.0", f"JIRA FIELDS DEBUG - {story_id}\n")
            text_widget.insert(tk.END, "="*80 + "\n\n")
            
            # Sección: Campos con contenido (los importantes)
            text_widget.insert(tk.END, "📋 CUSTOM FIELDS WITH CONTENT (Potential Acceptance Criteria fields)\n")
            text_widget.insert(tk.END, "="*80 + "\n\n")
            
            fields_with_content = all_fields.get('with_content', {})
            if fields_with_content:
                for field_name, value in sorted(fields_with_content.items()):
                    # Resaltar campos que probablemente sean acceptance criteria
                    if 'acceptance' in field_name.lower() or 'criteria' in field_name.lower() or 'ac' in field_name.lower():
                        text_widget.insert(tk.END, f"⭐ {field_name}:\n", 'highlight')
                    else:
                        text_widget.insert(tk.END, f"{field_name}:\n")
                    text_widget.insert(tk.END, f"  {value}\n\n")
            else:
                text_widget.insert(tk.END, "  No custom fields with content found\n\n")
            
            # Sección: Campos vacíos
            text_widget.insert(tk.END, "\n" + "="*80 + "\n")
            text_widget.insert(tk.END, "📭 EMPTY CUSTOM FIELDS (Not used in this story)\n")
            text_widget.insert(tk.END, "="*80 + "\n\n")
            
            empty_fields = all_fields.get('empty', [])
            if empty_fields:
                # Mostrar en columnas
                for i, field in enumerate(sorted(empty_fields)):
                    text_widget.insert(tk.END, f"  {field}\n")
            else:
                text_widget.insert(tk.END, "  No empty fields\n")
            
            # Sección: Campos del sistema
            text_widget.insert(tk.END, "\n" + "="*80 + "\n")
            text_widget.insert(tk.END, "⚙️ SYSTEM FIELDS (Standard Jira fields)\n")
            text_widget.insert(tk.END, "="*80 + "\n\n")
            
            system_fields = all_fields.get('system', [])
            if system_fields:
                text_widget.insert(tk.END, "  " + ", ".join(sorted(system_fields)) + "\n")
            
            # Instrucciones
            text_widget.insert(tk.END, "\n\n" + "="*80 + "\n")
            text_widget.insert(tk.END, "💡 INSTRUCTIONS\n")
            text_widget.insert(tk.END, "="*80 + "\n\n")
            text_widget.insert(tk.END, "1. Look for fields marked with ⭐ (likely acceptance criteria)\n")
            text_widget.insert(tk.END, "2. Copy the field name (e.g., customfield_10054)\n")
            text_widget.insert(tk.END, "3. Go to File → Settings\n")
            text_widget.insert(tk.END, "4. Paste in 'Acceptance Criteria Field'\n")
            text_widget.insert(tk.END, "5. You can add multiple fields separated by comma\n")
            text_widget.insert(tk.END, "   Example: customfield_10054,customfield_10000\n")
            
            # Configurar tag para highlight
            text_widget.tag_config('highlight', foreground='green', font=('Courier', 9, 'bold'))
            
            text_widget.config(state="disabled")
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Error getting fields:\n\n{str(e)}"
            )
    
    def _on_provider_change(self, event=None) -> None:
        """Actualiza los modelos disponibles cuando cambia el proveedor."""
        provider = self.provider_var.get()
        models = self.models_by_provider.get(provider, [])
        
        # Actualizar combobox del tab Single Story
        self.model_combo['values'] = models
        
        # Actualizar combobox del tab Sprint Analysis
        if hasattr(self, 'sprint_model_combo'):
            self.sprint_model_combo['values'] = models
        
        # Seleccionar primer modelo si hay modelos disponibles
        if models:
            self.model_var.set(models[0])
    
    def _get_full_model_name(self) -> str:
        """Obtiene el nombre completo del modelo con el prefijo del proveedor."""
        provider = self.provider_var.get()
        model = self.model_var.get()
        
        # LiteLLM requiere el formato: proveedor/modelo para algunos casos
        if provider == "Anthropic":
            return model  # Los modelos de Anthropic ya tienen el formato completo
        elif provider == "Groq (Free)":
            return f"groq/{model}"  # Groq necesita el prefijo
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
                if not self.jira_client:
                    self.jira_client = JiraClient.from_env()
                self.ai_analyzer = AIAnalyzer(
                    model=self._get_full_model_name(),
                    language=self.i18n.language
                )
            except Exception as e:
                self.status_var.set(self.i18n.get("status_error"))
                messagebox.showerror(
                    self.i18n.get("error"),
                    self.i18n.get("error_connection", error=str(e))
                )
                return
        
        # Si no hay datos cargados o el story ID cambió, obtener de Jira
        if not self.current_story_data or self.current_story_data['key'] != story_id:
            # Limpiar salida anterior
            self.output_text.clear()
            self.conversation_history = []
            self.current_story_data = None
            self.followup_button.config(state="disabled")
            self.export_button.config(state="disabled")
            self.post_to_jira_button.config(state="disabled")
            self.generate_tests_button.config(state="disabled")
            
            self.status_var.set(self.i18n.get("status_fetching", story_id=story_id))
            self.analyze_button.config(state="disabled")
            self.root.update()
            
            try:
                # Obtener notas del usuario
                user_notes = self.user_notes_text.get("1.0", tk.END).strip()
                
                # Obtener historia de Jira
                story_data = self.jira_client.get_user_story(story_id)
                
                # Agregar notas del usuario al story_data si existen
                if user_notes:
                    story_data['user_notes'] = user_notes
                
                self.current_story_data = story_data
                
            except Exception as e:
                messagebox.showerror(
                    self.i18n.get("error"), 
                    self.i18n.get("error_analysis", error=str(e))
                )
                self.status_var.set(self.i18n.get("status_error"))
                self.analyze_button.config(state="normal")
                return
        else:
            # Ya tenemos los datos, solo limpiar el análisis anterior si existe
            # pero mantener la información de Jira
            pass
        
        self.analyze_button.config(state="disabled")
        
        try:
            provider = self.provider_var.get()
            model = self.model_var.get()
            self.status_var.set(self.i18n.get("status_analyzing", story_id=story_id, provider=provider, model=model))
            self.root.update()
            
            # Actualizar modelo si cambió
            self.ai_analyzer.model = self._get_full_model_name()
            self.ai_analyzer.language = self.i18n.language
            
            # Check if Blaze Rules Context mode is enabled
            use_kb_context = False
            if self.analysis_mode_var.get() == "blaze":
                use_kb_context = True
                self.output_text.append_text(f"\n{'='*80}\n", 'heading')
                self.output_text.append_text("🔍 BLAZE RULES CONTEXT MODE\n", 'heading')
                self.output_text.append_text(f"{'='*80}\n\n", 'heading')
                self.output_text.append_text("This mode will generate a Kiro prompt that you can use in the Blaze Java project.\n\n", 'normal')
                self.output_text.append_text(f"{'='*80}\n\n", 'normal')
            
            # Si ya hay contenido (fetch previo), agregar separador
            current_content = self.output_text.get_all_text().strip()
            if current_content and not use_kb_context:
                self.output_text.append_text(f"\n\n{'='*80}\n", 'normal')
                self.output_text.append_text("AI ANALYSIS\n", 'normal')
                self.output_text.append_text(f"{'='*80}\n\n", 'normal')
            elif not current_content:
                # Mostrar encabezado de la historia
                self._display_story_header(self.current_story_data)
            
            # Acumular contenido durante streaming
            accumulated_content = []
            
            # Callback para actualizar UI en tiempo real
            def stream_callback(chunk: str):
                accumulated_content.append(chunk)
                self.output_text.append_text(chunk, 'normal')
                self.root.update()
            
            # Analizar con IA (con streaming)
            analysis = self.ai_analyzer.analyze_story(
                self.current_story_data, 
                callback=stream_callback,
                use_kb_context=use_kb_context
            )
            
            # Si es modo Blaze, extraer y guardar el prompt de Kiro
            if use_kb_context:
                # Extraer el prompt de Kiro del análisis
                if "PROMPT FOR KIRO:" in analysis:
                    parts = analysis.split("PROMPT FOR KIRO:")
                    if len(parts) > 1:
                        self.last_kiro_prompt = parts[1].strip()
                        # Mostrar botón de copiar
                        self.copy_kiro_prompt_button.grid()
                        self.copy_kiro_prompt_button.config(state="normal")
            else:
                # Ocultar botón si no es modo Blaze
                self.copy_kiro_prompt_button.grid_remove()
                self.last_kiro_prompt = None
            
            # Guardar en historial
            self.conversation_history.append({
                "role": "assistant",
                "content": analysis
            })
            
            self.status_var.set(self.i18n.get("status_completed", story_id=story_id))
            
            # Habilitar campo de seguimiento
            self.followup_button.config(state="normal")
            self.export_button.config(state="normal")
            self.post_to_jira_button.config(state="normal")
            self.generate_tests_button.config(state="normal")
            
        except Exception as e:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("error_analysis", error=str(e))
            )
            self.status_var.set(self.i18n.get("status_error"))
        finally:
            self.analyze_button.config(state="normal")
    
    def _generate_test_cases(self) -> None:
        """Genera test cases en formato Gherkin para la historia actual."""
        if not self.current_story_data:
            messagebox.showwarning(
                self.i18n.get("warning"),
                self.i18n.get("warning_no_analysis")
            )
            return
        
        # Confirmar que se va a generar
        if not messagebox.askyesno(
            "Generate Test Cases",
            f"Generate test cases in Gherkin format for {self.current_story_data['key']}?"
        ):
            return
        
        self.status_var.set(self.i18n.get("status_generating_tests"))
        self.generate_tests_button.config(state="disabled")
        self.root.update()
        
        try:
            # Agregar separador en el output
            self.output_text.append_text(f"\n\n{'='*80}\n", 'normal')
            self.output_text.append_text("TEST CASES (GHERKIN FORMAT)\n", 'normal')
            self.output_text.append_text(f"{'='*80}\n\n", 'normal')
            
            # Callback para streaming
            def stream_callback(chunk: str):
                self.output_text.append_text(chunk, 'normal')
                self.root.update()
            
            # Generar test cases
            test_cases = self.ai_analyzer.generate_test_cases(
                self.current_story_data,
                callback=stream_callback
            )
            
            self.status_var.set(f"Test cases generated for {self.current_story_data['key']}")
            
        except Exception as e:
            messagebox.showerror(
                self.i18n.get("error"),
                f"Error generating test cases:\n\n{str(e)}"
            )
            self.status_var.set(self.i18n.get("status_error"))
        finally:
            self.generate_tests_button.config(state="normal")
    
    def _display_story_header(self, story_data: dict) -> None:
        """
        Muestra el encabezado de la historia.
        
        Args:
            story_data: Datos de la historia
        """
        header = f"""{'='*80}
USER STORY: {story_data['key']}
{'='*80}

Title: {story_data['title']}
Status: {story_data['status']}
Priority: {story_data['priority']}

{'='*80}

"""
        self.output_text.append_text(header, 'normal')
    
    def _send_followup(self) -> None:
        """Envía una pregunta de seguimiento a la IA."""
        question = self.followup_entry.get().strip()
        
        if not question:
            return
        
        if not self.current_story_data:
            messagebox.showwarning(
                self.i18n.get("warning"),
                self.i18n.get("warning_no_analysis")
            )
            return
        
        # Limpiar campo de entrada
        self.followup_entry.delete(0, tk.END)
        
        # Mostrar pregunta del usuario
        self.output_text.append_text(f"\n\n{'='*80}\n", 'separator')
        self.output_text.append_text(f"USER: {question}\n", 'user_label')
        self.output_text.append_text(f"{'='*80}\n\n", 'separator')
        
        # Deshabilitar botón mientras procesa
        self.followup_button.config(state="disabled")
        self.status_var.set(self.i18n.get("status_processing"))
        self.root.update()
        
        try:
            # Callback para streaming
            def stream_callback(chunk: str):
                self.output_text.append_text(chunk, 'normal')
                self.root.update()
            
            # Enviar pregunta de seguimiento
            response = self.ai_analyzer.followup_question(
                story_data=self.current_story_data,
                conversation_history=self.conversation_history,
                question=question,
                callback=stream_callback
            )
            
            # Actualizar historial
            self.conversation_history.append({"role": "user", "content": question})
            self.conversation_history.append({"role": "assistant", "content": response})
            
            self.status_var.set(self.i18n.get("status_ready"))
            
        except Exception as e:
            messagebox.showerror(
                self.i18n.get("error"),
                self.i18n.get("error_followup", error=str(e))
            )
            self.status_var.set(self.i18n.get("status_error"))
        finally:
            self.followup_button.config(state="normal")
    
    def _export_analysis(self) -> None:
        """Exporta el análisis a un archivo."""
        if not self.current_story_data:
            messagebox.showwarning(
                self.i18n.get("warning"),
                self.i18n.get("warning_no_analysis")
            )
            return
        
        # Obtener contenido del análisis
        content = self.output_text.get_all_text()
        
        if not content.strip():
            messagebox.showwarning(
                self.i18n.get("warning"),
                self.i18n.get("warning_empty_analysis")
            )
            return
        
        # Generar nombre de archivo sugerido
        story_id = self.current_story_data['key'].replace('-', '_')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"analysis_{story_id}_{timestamp}"
        
        # Abrir diálogo para guardar archivo
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            initialfile=default_filename,
            filetypes=[
                (self.i18n.get("pdf_files"), "*.pdf"),
                (self.i18n.get("word_files"), "*.docx"),
                (self.i18n.get("text_files"), "*.txt"),
                (self.i18n.get("markdown_files"), "*.md"),
                (self.i18n.get("all_files"), "*.*")
            ],
            title=self.i18n.get("export_title")
        )
        
        if filename:
            try:
                # Determinar formato por extensión
                ext = os.path.splitext(filename)[1].lower()
                
                if ext == '.pdf':
                    ExportManager.export_to_pdf(content, filename, self.current_story_data['key'])
                elif ext == '.docx':
                    ExportManager.export_to_docx(content, filename, self.current_story_data['key'])
                else:
                    # Exportar como texto plano
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(content)
                
                messagebox.showinfo(
                    self.i18n.get("success"),
                    self.i18n.get("export_success", filename=os.path.basename(filename))
                )
                self.status_var.set(self.i18n.get("status_exported", filename=os.path.basename(filename)))
                
            except Exception as e:
                messagebox.showerror(
                    self.i18n.get("error"),
                    self.i18n.get("error_export", error=str(e))
                )
                self.status_var.set(self.i18n.get("status_error"))
    
    def _copy_kiro_prompt(self) -> None:
        """Copia el prompt de Kiro al portapapeles."""
        if not self.last_kiro_prompt:
            messagebox.showwarning(
                "Warning",
                "No Kiro prompt available. Please analyze a story in Blaze Rules Context mode first."
            )
            return
        
        try:
            # Copiar al portapapeles
            self.root.clipboard_clear()
            self.root.clipboard_append(self.last_kiro_prompt)
            self.root.update()  # Necesario para que el clipboard persista
            
            messagebox.showinfo(
                "Success",
                "Kiro prompt copied to clipboard!\n\nYou can now paste it in Kiro when you open the Blaze Java project."
            )
            self.status_var.set("✅ Kiro prompt copied to clipboard")
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to copy to clipboard: {str(e)}"
            )
    
    def _open_post_to_jira_dialog(self) -> None:
        """Abre un diálogo para editar y publicar el comentario en Jira."""
        if not self.current_story_data:
            messagebox.showwarning(
                self.i18n.get("warning"),
                self.i18n.get("warning_no_analysis")
            )
            return
        
        # Obtener contenido del análisis
        content = self.output_text.get_all_text()
        
        if not content.strip():
            messagebox.showwarning(
                self.i18n.get("warning"),
                self.i18n.get("warning_empty_analysis")
            )
            return
        
        # Crear ventana de diálogo
        dialog = tk.Toplevel(self.root)
        dialog.title(self.i18n.get("edit_comment_title"))
        dialog.geometry("800x600")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Frame principal
        main_frame = ttk.Frame(dialog, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label
        ttk.Label(
            main_frame,
            text=self.i18n.get("comment_preview_label"),
            font=("Arial", 10, "bold")
        ).pack(anchor=tk.W, pady=(0, 5))
        
        # Text widget editable con scrollbar
        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        comment_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            yscrollcommand=scrollbar.set,
            font=("Courier", 10)
        )
        comment_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=comment_text.yview)
        
        # Convertir a formato Jira y mostrar
        from src.jira_formatter import prepare_analysis_for_jira
        jira_formatted = prepare_analysis_for_jira(content, self.current_story_data['key'])
        comment_text.insert("1.0", jira_formatted)
        
        # Frame de botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        def post_comment():
            """Publica el comentario editado en Jira."""
            edited_comment = comment_text.get("1.0", tk.END).strip()
            
            if not edited_comment:
                messagebox.showwarning(
                    self.i18n.get("warning"),
                    self.i18n.get("warning_empty_analysis")
                )
                return
            
            # Confirmar antes de publicar
            if messagebox.askyesno(
                self.i18n.get("confirm_post_title"),
                self.i18n.get("confirm_post_message", story_id=self.current_story_data['key'])
            ):
                try:
                    self.status_var.set(
                        self.i18n.get("status_posting_comment", story_id=self.current_story_data['key'])
                    )
                    dialog.update()
                    
                    # Publicar comentario
                    self.jira_client.post_comment(self.current_story_data['key'], edited_comment)
                    
                    self.status_var.set(
                        self.i18n.get("status_comment_posted", story_id=self.current_story_data['key'])
                    )
                    
                    messagebox.showinfo(
                        self.i18n.get("success"),
                        self.i18n.get("status_comment_posted", story_id=self.current_story_data['key'])
                    )
                    
                    dialog.destroy()
                    
                except Exception as e:
                    messagebox.showerror(
                        self.i18n.get("error"),
                        self.i18n.get("error_post_comment", error=str(e))
                    )
                    self.status_var.set(self.i18n.get("status_error"))
        
        # Botones
        ttk.Button(
            button_frame,
            text=self.i18n.get("post_comment_button"),
            command=post_comment
        ).pack(side=tk.RIGHT, padx=(5, 0))
        
        ttk.Button(
            button_frame,
            text=self.i18n.get("cancel_button"),
            command=dialog.destroy
        ).pack(side=tk.RIGHT)
    
    def _analyze_sprint(self) -> None:
        """Analiza múltiples historias de usuario como un sprint."""
        story_ids_text = self.story_ids_text.get("1.0", tk.END).strip()
        
        if not story_ids_text:
            messagebox.showwarning(
                self.i18n.get("warning"), 
                self.i18n.get("warning_empty_stories")
            )
            return
        
        # Parsear IDs (separados por coma, espacio o línea)
        import re
        story_ids = re.split(r'[,\s\n]+', story_ids_text)
        story_ids = [sid.strip() for sid in story_ids if sid.strip()]
        
        if len(story_ids) < 1:
            messagebox.showwarning(
                self.i18n.get("warning"),
                "Please enter at least 1 Story ID for sprint analysis"
            )
            return
        
        # Inicializar clientes si no existen
        if not self.jira_client or not self.ai_analyzer:
            try:
                self.status_var.set(self.i18n.get("status_connecting"))
                self.root.update()
                self.jira_client = JiraClient.from_env()
                self.ai_analyzer = AIAnalyzer(
                    model=self._get_full_model_name(),
                    language=self.i18n.language
                )
            except Exception as e:
                self.status_var.set(self.i18n.get("status_error"))
                messagebox.showerror(
                    self.i18n.get("error"),
                    self.i18n.get("error_connection", error=str(e))
                )
                return
        
        # Limpiar salida anterior
        self.sprint_output_text.clear()
        self.current_sprint_data = None
        self.export_sprint_button.config(state="disabled")
        
        # Si está marcado "Include child issues", expandir la lista
        all_story_ids = []
        if self.include_children_var.get():
            self.status_var.set(self.i18n.get("status_fetching_children"))
            self.root.update()
            
            for parent_id in story_ids:
                all_story_ids.append(parent_id)
                try:
                    children = self.jira_client.get_child_issues(parent_id)
                    if children:
                        self.sprint_output_text.append_text(
                            f"📋 Found {len(children)} child issues for {parent_id}: {', '.join(children)}\n\n",
                            'normal'
                        )
                        all_story_ids.extend(children)
                except Exception as e:
                    self.sprint_output_text.append_text(
                        f"⚠️ Warning: Could not fetch children for {parent_id}: {str(e)}\n\n",
                        'normal'
                    )
        else:
            all_story_ids = story_ids
        
        # Remover duplicados manteniendo el orden
        seen = set()
        unique_story_ids = []
        for sid in all_story_ids:
            if sid not in seen:
                seen.add(sid)
                unique_story_ids.append(sid)
        
        self.status_var.set(self.i18n.get("status_fetching_multiple", count=len(unique_story_ids)))
        self.analyze_sprint_button.config(state="disabled")
        self.root.update()
        
        try:
            # Obtener todas las historias de Jira
            stories_data = []
            for story_id in unique_story_ids:
                try:
                    story_data = self.jira_client.get_user_story(story_id)
                    stories_data.append(story_data)
                except Exception as e:
                    self.sprint_output_text.append_text(
                        f"⚠️ Warning: Could not fetch {story_id}: {str(e)}\n\n",
                        'normal'
                    )
            
            if not stories_data:
                raise Exception("No stories could be fetched from Jira")
            
            self.current_sprint_data = stories_data
            
            provider = self.provider_var.get()
            model = self.model_var.get()
            self.status_var.set(self.i18n.get("status_analyzing_sprint", count=len(stories_data)))
            self.root.update()
            
            # Actualizar modelo si cambió
            self.ai_analyzer.model = self._get_full_model_name()
            self.ai_analyzer.language = self.i18n.language
            
            # Mostrar encabezado
            self._display_sprint_header(stories_data)
            
            # Callback para streaming
            def stream_callback(chunk: str):
                self.sprint_output_text.append_text(chunk, 'normal')
                self.root.update()
            
            # Analizar sprint con IA
            self.status_var.set(self.i18n.get("status_generating_plan"))
            analysis = self.ai_analyzer.analyze_sprint(stories_data, callback=stream_callback)
            
            self.status_var.set(self.i18n.get("status_completed_sprint", count=len(stories_data)))
            
            # Habilitar exportar
            self.export_sprint_button.config(state="normal")
            
        except Exception as e:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("error_analysis", error=str(e))
            )
            self.status_var.set(self.i18n.get("status_error"))
        finally:
            self.analyze_sprint_button.config(state="normal")
    
    def _display_sprint_header(self, stories_data: list) -> None:
        """
        Muestra el encabezado del análisis de sprint.
        
        Args:
            stories_data: Lista de datos de historias
        """
        header = f"""{'='*80}
SPRINT ANALYSIS: {len(stories_data)} Stories
{'='*80}

Stories:
"""
        for story in stories_data:
            header += f"  - {story['key']}: {story['title']} [{story['priority']}]\n"
        
        header += f"\n{'='*80}\n\n"
        self.sprint_output_text.append_text(header, 'normal')
    
    def _export_sprint_analysis(self) -> None:
        """Exporta el análisis de sprint a un archivo."""
        if not self.current_sprint_data:
            messagebox.showwarning(
                self.i18n.get("warning"),
                self.i18n.get("warning_no_analysis")
            )
            return
        
        # Obtener contenido del análisis
        content = self.sprint_output_text.get_all_text()
        
        if not content.strip():
            messagebox.showwarning(
                self.i18n.get("warning"),
                self.i18n.get("warning_empty_analysis")
            )
            return
        
        # Generar nombre de archivo sugerido
        story_ids = [s['key'].replace('-', '_') for s in self.current_sprint_data[:3]]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"sprint_analysis_{'_'.join(story_ids)}_etc_{timestamp}"
        
        # Abrir diálogo para guardar archivo
        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            initialfile=default_filename,
            filetypes=[
                (self.i18n.get("pdf_files"), "*.pdf"),
                (self.i18n.get("word_files"), "*.docx"),
                (self.i18n.get("text_files"), "*.txt"),
                (self.i18n.get("markdown_files"), "*.md"),
                (self.i18n.get("all_files"), "*.*")
            ],
            title=self.i18n.get("export_title")
        )
        
        if filename:
            try:
                # Determinar formato por extensión
                ext = os.path.splitext(filename)[1].lower()
                
                sprint_title = f"Sprint Analysis ({len(self.current_sprint_data)} stories)"
                
                if ext == '.pdf':
                    ExportManager.export_to_pdf(content, filename, sprint_title)
                elif ext == '.docx':
                    ExportManager.export_to_docx(content, filename, sprint_title)
                else:
                    # Exportar como texto plano
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(content)
                
                messagebox.showinfo(
                    self.i18n.get("success"),
                    self.i18n.get("export_success", filename=os.path.basename(filename))
                )
                self.status_var.set(self.i18n.get("status_exported", filename=os.path.basename(filename)))
                
            except Exception as e:
                messagebox.showerror(
                    self.i18n.get("error"),
                    self.i18n.get("error_export", error=str(e))
                )
                self.status_var.set(self.i18n.get("status_error"))

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
