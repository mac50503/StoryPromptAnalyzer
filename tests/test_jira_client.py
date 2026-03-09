"""Tests para el cliente de Jira."""

from unittest.mock import Mock, patch
from src.jira_client import JiraClient


def test_jira_client_initialization() -> None:
    """Test de inicialización del cliente."""
    client = JiraClient(
        url="https://test.atlassian.net",
        email="test@test.com",
        api_token="test_token"
    )
    assert client.jira is not None


@patch('src.jira_client.JIRA')
def test_get_user_story(mock_jira: Mock) -> None:
    """Test de obtención de historia de usuario."""
    # Mock del issue
    mock_issue = Mock()
    mock_issue.key = "TEST-123"
    mock_issue.fields.summary = "Test Story"
    mock_issue.fields.description = "Test Description"
    mock_issue.fields.comment.comments = []
    mock_issue.fields.labels = ["test"]
    mock_issue.fields.status.name = "To Do"
    mock_issue.fields.priority.name = "High"
    
    mock_jira_instance = Mock()
    mock_jira_instance.issue.return_value = mock_issue
    mock_jira.return_value = mock_jira_instance
    
    client = JiraClient("https://test.atlassian.net", "test@test.com", "token")
    story = client.get_user_story("TEST-123")
    
    assert story["key"] == "TEST-123"
    assert story["title"] == "Test Story"
    assert story["status"] == "To Do"
