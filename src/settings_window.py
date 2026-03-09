"""Ventana de configuración para editar parámetros del .env"""

import tkinter as tk
from tkinter import ttk, messagebox
import os
from dotenv import load_dotenv, set_key
from typing import Callable, Optional


class SettingsWindow:
    """Ventana de diálogo para configurar parámetros."""

    def __init__(self, parent: tk.Tk, on_save_callback: Optional[Callable] = None, i18n=None):
        """
        Inicializa la ventana de configuración.
        
        Args:
            parent: Ventana padre
            on_save_callback: Función a llamar cuando se guarden los cambios
            i18n: Sistema de traducciones
        """
        self.parent = parent
        self.on_save_callback = on_save_callback
        self.i18n = i18n
        self.env_file = ".env"
        
        # Crear ventana
        self.window = tk.Toplevel(parent)
        self.window.title(self.i18n.get("settings_title"))
        self.window.geometry("650x500")
        self.window.resizable(True, True)
        
        # Hacer modal
        self.window.transient(parent)
        self.window.grab_set()
        
        self._setup_ui()
        self._load_current_values()
        
        # Centrar ventana
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (self.window.winfo_width() // 2)
        y = (self.window.winfo_screenheight() // 2) - (self.window.winfo_height() // 2)
        self.window.geometry(f"+{x}+{y}")

    def _setup_ui(self) -> None:
        """Configura los elementos de la interfaz."""
        # Frame principal
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(
            main_frame,
            text=self.i18n.get("settings_header"),
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=(0, 20))
        
        # Canvas y scrollbar para el contenido
        canvas = tk.Canvas(main_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame para campos dentro del scrollable
        fields_frame = ttk.Frame(scrollable_frame)
        fields_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        # Sección Jira
        jira_label = ttk.Label(fields_frame, text=self.i18n.get("jira_section"), font=("Arial", 11, "bold"))
        jira_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        ttk.Label(fields_frame, text=self.i18n.get("jira_url")).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.jira_url_entry = ttk.Entry(fields_frame, width=50)
        self.jira_url_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        ttk.Label(fields_frame, text=self.i18n.get("jira_email")).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.jira_email_entry = ttk.Entry(fields_frame, width=50)
        self.jira_email_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        ttk.Label(fields_frame, text=self.i18n.get("jira_token")).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.jira_token_entry = ttk.Entry(fields_frame, width=50, show="*")
        self.jira_token_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Separador
        ttk.Separator(fields_frame, orient=tk.HORIZONTAL).grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        
        # Sección OpenAI
        openai_label = ttk.Label(fields_frame, text=self.i18n.get("openai_section"), font=("Arial", 11, "bold"))
        openai_label.grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        ttk.Label(fields_frame, text=self.i18n.get("openai_key")).grid(row=6, column=0, sticky=tk.W, pady=5)
        self.openai_key_entry = ttk.Entry(fields_frame, width=50, show="*")
        self.openai_key_entry.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Separador
        ttk.Separator(fields_frame, orient=tk.HORIZONTAL).grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        
        # Sección Anthropic
        anthropic_label = ttk.Label(fields_frame, text=self.i18n.get("anthropic_section"), font=("Arial", 11, "bold"))
        anthropic_label.grid(row=8, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        ttk.Label(fields_frame, text=self.i18n.get("anthropic_key")).grid(row=9, column=0, sticky=tk.W, pady=5)
        self.anthropic_key_entry = ttk.Entry(fields_frame, width=50, show="*")
        self.anthropic_key_entry.grid(row=9, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Separador
        ttk.Separator(fields_frame, orient=tk.HORIZONTAL).grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        
        # Sección General
        general_label = ttk.Label(fields_frame, text=self.i18n.get("general_section"), font=("Arial", 11, "bold"))
        general_label.grid(row=11, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        # Modelo por defecto
        ttk.Label(fields_frame, text=self.i18n.get("default_model")).grid(row=12, column=0, sticky=tk.W, pady=5)
        self.model_entry = ttk.Entry(fields_frame, width=50)
        self.model_entry.grid(row=12, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Configurar peso de columnas
        fields_frame.columnconfigure(1, weight=1)
        
        # Empaquetar canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Frame de botones (fuera del scroll)
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(button_frame, text=self.i18n.get("button_cancel"), command=self.window.destroy).pack(side=tk.RIGHT, padx=5)
        ttk.Button(button_frame, text=self.i18n.get("button_save"), command=self._save_and_close).pack(side=tk.RIGHT)
        
        # Bind mousewheel para scroll
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def _load_current_values(self) -> None:
        """Carga los valores actuales del archivo .env"""
        load_dotenv()
        
        self.jira_url_entry.insert(0, os.getenv("JIRA_URL", ""))
        self.jira_email_entry.insert(0, os.getenv("JIRA_EMAIL", ""))
        self.jira_token_entry.insert(0, os.getenv("JIRA_API_TOKEN", ""))
        self.openai_key_entry.insert(0, os.getenv("OPENAI_API_KEY", ""))
        self.anthropic_key_entry.insert(0, os.getenv("ANTHROPIC_API_KEY", ""))
        self.model_entry.insert(0, os.getenv("AI_MODEL", "gpt-4"))

    def _save_settings(self) -> None:
        """Guarda la configuración en el archivo .env"""
        try:
            # Crear archivo .env si no existe
            if not os.path.exists(self.env_file):
                with open(self.env_file, 'w') as f:
                    f.write("")
            
            # Guardar cada valor
            set_key(self.env_file, "JIRA_URL", self.jira_url_entry.get())
            set_key(self.env_file, "JIRA_EMAIL", self.jira_email_entry.get())
            set_key(self.env_file, "JIRA_API_TOKEN", self.jira_token_entry.get())
            set_key(self.env_file, "OPENAI_API_KEY", self.openai_key_entry.get())
            set_key(self.env_file, "ANTHROPIC_API_KEY", self.anthropic_key_entry.get())
            set_key(self.env_file, "AI_MODEL", self.model_entry.get())
            
            return True
            
        except Exception as e:
            messagebox.showerror(
                self.i18n.get("error"), 
                self.i18n.get("error_save_config", error=str(e))
            )
            return False
    
    def _save_and_close(self) -> None:
        """Guarda la configuración y cierra la ventana."""
        if self._save_settings():
            # Llamar callback si existe
            if self.on_save_callback:
                self.on_save_callback()
            
            # Cerrar ventana
            self.window.destroy()
