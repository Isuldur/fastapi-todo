"""Tests for the todo application."""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
TODO_ID = None  # pylint: disable=invalid-name


def test_create_todo():
    """Test creating a new todo item."""
    response = client.post("/todos", json={
        "title": "Tarea de prueba",
        "description": "Esto es una descripción"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Tarea de prueba"
    assert data["description"] == "Esto es una descripción"
    assert data["completed"] is False
    global TODO_ID  # pylint: disable=global-statement
    TODO_ID = data["id"]


def test_list_todos():
    """Test listing all todo items."""
    response = client.get("/todos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(todo["id"] == TODO_ID for todo in data)


def test_get_todo():
    """Test getting a specific todo item by ID."""
    response = client.get(f"/todos/{TODO_ID}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == TODO_ID
    assert data["title"] == "Tarea de prueba"


def test_update_todo():
    """Test updating a specific todo item."""
    response = client.put(f"/todos/{TODO_ID}", json={
        "title": "Tarea actualizada",
        "description": "Descripción actualizada",
        "completed": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Tarea actualizada"
    assert data["completed"] is True


def test_delete_todo():
    """Test deleting a specific todo item."""
    response = client.delete(f"/todos/{TODO_ID}")
    assert response.status_code == 200
    data = response.json()
    assert data["ok"] is True

    # Verificamos que ya no existe
    response_check = client.get(f"/todos/{TODO_ID}")
    assert response_check.status_code == 404
