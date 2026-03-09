"""Visualizador de texto enriquecido para análisis."""

import tkinter as tk
from tkinter import scrolledtext
import re


class RichTextViewer(scrolledtext.ScrolledText):
    """Widget de texto con formato enriquecido."""
    
    def __init__(self, parent, **kwargs):
        """
        Inicializa el visualizador.
        
        Args:
            parent: Widget padre
            **kwargs: Argumentos adicionales para ScrolledText
        """
        super().__init__(parent, **kwargs)
        
        # Configurar como no editable
        self.config(state='disabled', wrap=tk.WORD)
        
        # Definir estilos de texto
        self._setup_tags()
    
    def _setup_tags(self):
        """Configura los tags de formato."""
        # Texto normal - fuente más legible
        self.tag_config('normal', font=('Consolas', 10), foreground='#2c3e50')
    
    def append_text(self, text, tag='normal'):
        """
        Agrega texto con formato.
        
        Args:
            text: Texto a agregar
            tag: Tag de formato a aplicar
        """
        self.config(state='normal')
        self.insert(tk.END, text, tag)
        self.config(state='disabled')
        self.see(tk.END)
    
    def append_formatted(self, text):
        """
        Agrega texto con auto-detección de formato markdown.
        
        Args:
            text: Texto en formato markdown
        """
        self.config(state='normal')
        
        # Si el texto es muy corto (streaming), agregarlo sin formato
        if len(text) < 10:
            self.insert(tk.END, text, 'normal')
            self.config(state='disabled')
            self.see(tk.END)
            return
        
        lines = text.split('\n')
        for line in lines:
            # Detectar headers
            if line.startswith('# '):
                self.insert(tk.END, line[2:] + '\n', 'h1')
            elif line.startswith('## '):
                self.insert(tk.END, line[3:] + '\n', 'h2')
            elif line.startswith('### '):
                self.insert(tk.END, line[4:] + '\n', 'h3')
            
            # Detectar separadores
            elif line.strip().startswith('===') or line.strip().startswith('---'):
                self.insert(tk.END, line + '\n', 'separator')
            
            # Detectar listas numeradas
            elif re.match(r'^\d+\.\s', line):
                self.insert(tk.END, line + '\n', 'number')
            
            # Detectar listas con viñetas
            elif line.strip().startswith('- ') or line.strip().startswith('* '):
                self.insert(tk.END, line + '\n', 'bullet')
            
            # Detectar warnings/notes
            elif '⚠️' in line or 'WARNING' in line.upper():
                self.insert(tk.END, line + '\n', 'warning')
            elif 'ℹ️' in line or 'NOTE' in line.upper():
                self.insert(tk.END, line + '\n', 'note')
            
            # Detectar USER/AI labels
            elif line.startswith('USER:'):
                self.insert(tk.END, line + '\n', 'user_label')
            elif line.startswith('AI:') or line.startswith('ASSISTANT:'):
                self.insert(tk.END, line + '\n', 'ai_label')
            
            # Texto normal con detección de bold
            else:
                # Procesar bold (**texto**)
                parts = re.split(r'(\*\*.*?\*\*)', line)
                for part in parts:
                    if part.startswith('**') and part.endswith('**'):
                        self.insert(tk.END, part[2:-2], 'bold')
                    else:
                        self.insert(tk.END, part, 'normal')
                self.insert(tk.END, '\n', 'normal')
        
        self.config(state='disabled')
        self.see(tk.END)
    
    def clear(self):
        """Limpia todo el contenido."""
        self.config(state='normal')
        self.delete(1.0, tk.END)
        self.config(state='disabled')
    
    def get_all_text(self):
        """
        Obtiene todo el texto sin formato.
        
        Returns:
            Texto completo
        """
        return self.get(1.0, tk.END)
