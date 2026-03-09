"""Tests para el analizador de IA."""

from src.ai_analyzer import AIAnalyzer


def test_ai_analyzer_initialization() -> None:
    """Test de inicialización del analizador."""
    analyzer = AIAnalyzer(model="gpt-4")
    assert analyzer.model == "gpt-4"


def test_create_analysis_prompt() -> None:
    """Test de creación de prompt."""
    analyzer = AIAnalyzer()
    
    story_data = {
        "key": "TEST-123",
        "title": "Test Story",
        "description": "Test description",
        "acceptance_criteria": "Test criteria",
        "comments": ["Comment 1"],
        "labels": ["test"],
        "status": "To Do",
        "priority": "High"
    }
    
    prompt = analyzer.create_analysis_prompt(story_data)
    
    assert "TEST-123" in prompt
    assert "Test Story" in prompt
    assert "experto en desarrollo y arquitectura" in prompt
    assert "AMBIGÜEDADES" in prompt
