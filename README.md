# StoryPromptAnalyzer

Service that converts Jira user stories into structured AI prompts and generates requirement analysis reports to detect ambiguities, gaps, and potential improvements.

## Características

- Conexión a Jira para leer historias de usuario
- Análisis automático usando modelos de IA (OpenAI y Anthropic)
- Interfaz gráfica intuitiva
- Generación de reportes estructurados de análisis de requerimientos
- Identificación de ambigüedades, información faltante y riesgos

## Estructura del Proyecto

```
.
├── src/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada
│   ├── gui.py               # Interfaz gráfica
│   ├── jira_client.py       # Cliente de Jira
│   └── ai_analyzer.py       # Analizador con IA
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_jira_client.py
│   └── test_ai_analyzer.py
├── .env.example             # Plantilla de configuración
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Instalación

1. Clona el repositorio y navega al directorio

2. Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements-dev.txt
```

4. Configura las credenciales:
```bash
cp .env.example .env
```

5. Edita el archivo `.env` con tus credenciales:
   - **JIRA_URL**: URL de tu instancia de Jira (ej: https://tu-empresa.atlassian.net)
   - **JIRA_EMAIL**: Tu email de Jira
   - **JIRA_API_TOKEN**: Token de API de Jira ([Cómo obtenerlo](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/))
   - **OPENAI_API_KEY**: Tu clave de API de OpenAI
   - **ANTHROPIC_API_KEY**: Tu clave de API de Anthropic
   - **AI_MODEL**: Modelo a usar (gpt-4, gpt-3.5-turbo, claude-3-opus-20240229, etc.)

## Uso

### Ejecutar la aplicación

```bash
python src/main.py
```

O alternativamente:

```bash
python -m src.gui
```

### Usar la interfaz

1. Ingresa el ID de la historia de Jira (ej: PROJ-123)
2. Selecciona el modelo de IA que deseas usar
3. Haz clic en "Analizar Historia"
4. El análisis aparecerá en el visualizador de texto

### Modelos disponibles

- **OpenAI**: gpt-4, gpt-3.5-turbo
- **Anthropic**: claude-3-opus-20240229, claude-3-sonnet-20240229

## Análisis generado

El análisis incluye:

1. **Resumen del Requerimiento**: Reformulación clara del objetivo
2. **Estructura del Requerimiento**: Actores, funcionalidad, flujo de trabajo
3. **Ambigüedades Detectadas**: Puntos poco claros o imprecisos
4. **Información Faltante**: Criterios incompletos, casos edge, requisitos no funcionales
5. **Posibles Mejoras y Riesgos**: Sugerencias, riesgos técnicos, consideraciones de seguridad

## Desarrollo

### Ejecutar tests
```bash
pytest
```

### Formatear código
```bash
black src/ tests/
```

### Verificar estilo
```bash
flake8 src/ tests/
```

### Verificar tipos
```bash
mypy src/
```

## Seguridad

- Las credenciales se almacenan en el archivo `.env` que está excluido de Git
- Nunca compartas tu archivo `.env` o subas credenciales al repositorio
- Usa tokens de API con permisos mínimos necesarios

## Licencia

MIT
