"""Módulo principal de la aplicación Story Prompt Analyzer."""

import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gui import main

if __name__ == "__main__":
    main()
