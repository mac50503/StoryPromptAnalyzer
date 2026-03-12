"""Búsqueda y análisis de la base de conocimientos de Blaze Rules."""

import os
import re
from typing import Dict, List, Set, Optional
from pathlib import Path


class KnowledgeBaseSearch:
    """Busca y analiza información de la base de conocimientos de Blaze Rules."""
    
    def __init__(self, kb_path: str = "knowledge-base"):
        """
        Inicializa el buscador de base de conocimientos.
        
        Args:
            kb_path: Ruta a la carpeta knowledge-base
        """
        self.kb_path = Path(kb_path)
        self.functions_path = self.kb_path / "functions"
        self.ruleflows_path = self.kb_path / "by-ruleflow"
        self._function_cache = None
        
    def is_available(self) -> bool:
        """Verifica si la base de conocimientos está disponible."""
        return self.kb_path.exists() and self.functions_path.exists()
    
    def _load_function_list(self) -> List[Dict[str, str]]:
        """Carga la lista de todas las funciones disponibles con sus descripciones."""
        if self._function_cache is not None:
            return self._function_cache
        
        functions = []
        if not self.functions_path.exists():
            return functions
        
        for func_file in self.functions_path.glob("*.md"):
            func_name = func_file.stem
            try:
                content = func_file.read_text(encoding='utf-8')
                # Extraer primera línea de descripción si existe
                lines = content.split('\n')
                description = ""
                for line in lines[1:10]:  # Buscar en las primeras líneas
                    if line.strip() and not line.startswith('#'):
                        description = line.strip()
                        break
                
                functions.append({
                    'name': func_name,
                    'description': description,
                    'file': str(func_file)
                })
            except:
                continue
        
        self._function_cache = functions
        return functions
    
    def search_functions_by_keywords(self, keywords: List[str]) -> List[Dict[str, str]]:
        """
        Busca funciones que coincidan con palabras clave, priorizando múltiples coincidencias.
        
        Args:
            keywords: Lista de palabras clave para buscar
            
        Returns:
            Lista de funciones ordenadas por relevancia (más coincidencias primero)
        """
        all_functions = self._load_function_list()
        scored_functions = []
        
        for func in all_functions:
            func_text = f"{func['name']} {func['description']}".lower()
            
            # Contar cuántas keywords coinciden
            match_count = 0
            matched_keywords = []
            
            for keyword in keywords:
                if keyword.lower() in func_text:
                    match_count += 1
                    matched_keywords.append(keyword)
            
            # Solo incluir funciones con al menos una coincidencia
            if match_count > 0:
                scored_functions.append({
                    **func,
                    'match_count': match_count,
                    'matched_keywords': matched_keywords
                })
        
        # Ordenar por número de coincidencias (más coincidencias primero)
        scored_functions.sort(key=lambda x: x['match_count'], reverse=True)
        
        return scored_functions
    
    def extract_function_names(self, text: str) -> Set[str]:
        """
        Extrae nombres de funciones y rulesets mencionados en el texto.
        
        Args:
            text: Texto de la historia de usuario
            
        Returns:
            Set de nombres de funciones encontradas
        """
        # Patrones para detectar funciones y rulesets
        patterns = [
            r'\b(fcn[A-Z][a-zA-Z0-9]+)\b',  # fcnFunctionName
            r'\b(rs[A-Z][a-zA-Z0-9_]+)\b',  # rsFunctionName
            r'\b(rst[A-Z][a-zA-Z0-9_]+)\b', # rstFunctionName
        ]
        
        found_functions = set()
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            found_functions.update(matches)
        
        return found_functions
    
    def extract_domain_keywords(self, text: str) -> List[str]:
        """
        Extrae palabras clave del dominio de negocio de la historia.
        
        Args:
            text: Texto de la historia
            
        Returns:
            Lista de palabras clave relevantes ordenadas por especificidad
        """
        # Palabras clave organizadas por especificidad (más específicas primero)
        # Formato: (keyword, priority_weight)
        domain_keywords = [
            # Muy específicas (peso 3)
            ('holiday pay', 3), ('festivo', 3), ('feriado', 3),
            ('red eye', 3), ('redeye', 3),
            ('per diem', 3), ('perdiem', 3),
            ('staff bank', 3),
            ('longevity', 3), ('antiguedad', 3), ('antigüedad', 3),
            ('experience pay', 3),
            ('initial operating experience', 3), ('ioe', 3),
            ('deadhead', 3), ('muerto', 3),
            ('charter', 3),
            ('mileage', 3), ('millaje', 3),
            ('productivity pay', 3),
            ('split guarantee', 3), ('split guaranty', 3),
            
            # Específicas (peso 2)
            ('reserve', 2), ('reserva', 2),
            ('ron', 2), ('overnight', 2), ('pernocta', 2),
            ('premium', 2), ('bonus', 2),
            ('rig', 2), ('guarantee', 2), ('garantia', 2), ('garantía', 2),
            ('credit', 2), ('credito', 2), ('crédito', 2),
            ('bucket', 2), ('category', 2), ('categoria', 2), ('categoría', 2),
            ('conus', 2), ('oconus', 2),
            ('qualification', 2), ('calificacion', 2), ('calificación', 2),
            ('training', 2), ('entrenamiento', 2),
            ('legality', 2), ('legalidad', 2),
            ('faa rest', 2), ('descanso', 2),
            ('schedule period', 2), ('programacion', 2), ('programación', 2),
            ('duty period', 2), ('periodo de servicio', 2),
            
            # Genéricas (peso 1)
            ('pay', 1), ('pago', 1), ('salary', 1), ('salario', 1),
            ('duty', 1), ('servicio', 1),
            ('period', 1), ('periodo', 1),
            ('leg', 1), ('tramo', 1),
            ('flight', 1), ('vuelo', 1),
            ('trip', 1), ('viaje', 1),
            ('crew', 1), ('tripulacion', 1), ('tripulación', 1),
            ('schedule', 1), ('horario', 1),
            ('holiday', 1),
        ]
        
        found_keywords = []
        text_lower = text.lower()
        
        # Buscar keywords y guardar con su peso
        for keyword, weight in domain_keywords:
            if keyword in text_lower:
                found_keywords.append((keyword, weight))
        
        # Ordenar por peso (más específicas primero) y luego alfabéticamente
        found_keywords.sort(key=lambda x: (-x[1], x[0]))
        
        # Retornar solo los keywords, sin el peso
        return [kw for kw, _ in found_keywords]
    
    def get_function_info(self, function_name: str) -> Optional[Dict[str, any]]:
        """
        Obtiene información de una función desde la base de conocimientos.
        
        Args:
            function_name: Nombre de la función
            
        Returns:
            Diccionario con información de la función o None si no existe
        """
        function_file = self.functions_path / f"{function_name}.md"
        
        if not function_file.exists():
            return None
        
        try:
            content = function_file.read_text(encoding='utf-8')
            
            # Extraer información básica del markdown
            info = {
                'name': function_name,
                'file_path': str(function_file),
                'content': content[:500],  # Primeros 500 caracteres
                'used_by_ruleflows': self._find_ruleflows_using_function(function_name)
            }
            
            return info
        except Exception as e:
            return None
    
    def _find_ruleflows_using_function(self, function_name: str) -> List[str]:
        """
        Encuentra qué RuleFlows usan una función específica.
        
        Args:
            function_name: Nombre de la función
            
        Returns:
            Lista de nombres de RuleFlows que usan la función
        """
        ruleflows = []
        
        if not self.ruleflows_path.exists():
            return ruleflows
        
        # Buscar en archivos de RuleFlows
        for ruleflow_file in self.ruleflows_path.glob("CssIf*.md"):
            try:
                content = ruleflow_file.read_text(encoding='utf-8')
                if function_name in content:
                    ruleflow_name = ruleflow_file.stem
                    ruleflows.append(ruleflow_name)
            except:
                continue
        
        return ruleflows
    
    def analyze_story_context(self, story_data: Dict[str, any]) -> Dict[str, any]:
        """
        Analiza una historia y extrae contexto de la base de conocimientos.
        
        Args:
            story_data: Datos de la historia de Jira
            
        Returns:
            Diccionario con contexto encontrado
        """
        if not self.is_available():
            return {
                'available': False,
                'message': 'Knowledge base not found'
            }
        
        # Combinar todo el texto de la historia
        full_text = f"{story_data.get('title', '')} {story_data.get('description', '')} {story_data.get('acceptance_criteria', '')}"
        
        # 1. Buscar funciones mencionadas explícitamente
        mentioned_functions = self.extract_function_names(full_text)
        
        # 2. Extraer palabras clave del dominio
        domain_keywords = self.extract_domain_keywords(full_text)
        
        # 3. Buscar funciones relacionadas por palabras clave
        keyword_functions = []
        if domain_keywords and not mentioned_functions:
            keyword_functions = self.search_functions_by_keywords(domain_keywords)
            # Limitar a las 10 más relevantes
            keyword_functions = keyword_functions[:10]
        
        # Obtener información de funciones mencionadas explícitamente
        functions_info = []
        all_ruleflows = set()
        
        for func_name in mentioned_functions:
            func_info = self.get_function_info(func_name)
            if func_info:
                functions_info.append(func_info)
                all_ruleflows.update(func_info['used_by_ruleflows'])
        
        return {
            'available': True,
            'functions_found': functions_info,
            'keyword_matches': keyword_functions,
            'domain_keywords': domain_keywords,
            'affected_ruleflows': list(all_ruleflows),
            'total_functions': len(functions_info),
            'total_keyword_matches': len(keyword_functions),
            'total_ruleflows': len(all_ruleflows)
        }
    
    def format_context_for_prompt(self, context: Dict[str, any]) -> str:
        """
        Formatea el contexto de KB para incluir en el prompt del AI.
        
        Args:
            context: Contexto extraído de analyze_story_context()
            
        Returns:
            String formateado para incluir en el prompt
        """
        if not context.get('available'):
            return ""
        
        lines = ["\n<blaze_rules_context>"]
        
        # Funciones mencionadas explícitamente
        if context.get('functions_found'):
            lines.append(f"This story explicitly mentions {context['total_functions']} Blaze Rules functions/rulesets:")
            lines.append("")
            
            for func in context['functions_found']:
                lines.append(f"- {func['name']}")
                if func['used_by_ruleflows']:
                    lines.append(f"  Used by RuleFlows: {', '.join(func['used_by_ruleflows'])}")
        
        # Palabras clave del dominio encontradas
        if context.get('domain_keywords'):
            lines.append("")
            lines.append(f"Domain keywords detected: {', '.join(context['domain_keywords'][:10])}")
        
        # Funciones relacionadas por palabras clave
        if context.get('keyword_matches'):
            lines.append("")
            lines.append(f"Potentially related functions (based on keywords, top {len(context['keyword_matches'])}):")
            for func in context['keyword_matches']:
                lines.append(f"- {func['name']}")
        
        # RuleFlows afectados
        if context.get('affected_ruleflows'):
            lines.append("")
            lines.append(f"Affected RuleFlows ({context['total_ruleflows']}):")
            for rf in context['affected_ruleflows']:
                lines.append(f"- {rf}")
        
        lines.append("")
        lines.append("IMPORTANT: Use this context to:")
        lines.append("1. Identify which specific functions need to be modified")
        lines.append("2. Consider impact on related RuleFlows")
        lines.append("3. Suggest specific test cases for affected business rules")
        lines.append("4. Mention regression risks")
        lines.append("</blaze_rules_context>\n")
        
        return "\n".join(lines)
