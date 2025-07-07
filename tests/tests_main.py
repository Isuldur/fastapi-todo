"""Tests for the todo application."""
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_and_get_todo():
    """Test creating and retrieving a todo item."""
    # Crear tarea
    response = client.post("/todos", json={
        "title": "Test tarea",
        "description": "Descripción de prueba"
        })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test tarea"
    assert data["description"] == "Descripción de prueba"
    todo_id = data["id"]

    # Obtener tarea
    response_get = client.get(f"/todos/{todo_id}")
    assert response_get.status_code == 200
    data_get = response_get.json()
    assert data_get["id"] == todo_id
    assert data_get["title"] == "Test tarea"
