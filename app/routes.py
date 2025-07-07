"""Routes for the todo app."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todo

router = APIRouter()


# Dependency: abrir y cerrar la sesión con la base de datos
def get_db():
    """Get database session dependency."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Crear una tarea
@router.post("/todos")
def create_todo(
    title: str,
    description: str = "",
    db: Session = Depends(get_db)
):
    """Create a new todo item."""
    todo = Todo(title=title, description=description)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


# Listar todas las tareas
@router.get("/todos")
def get_all_todos(db: Session = Depends(get_db)):
    """Get all todo items."""
    return db.query(Todo).all()


# Obtener una tarea por ID
@router.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a specific todo item by ID."""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return todo


# Actualizar una tarea
@router.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    title: str,
    description: str,
    completed: bool,
    db: Session = Depends(get_db),
):
    """Update a specific todo item."""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    todo.title = title
    todo.description = description
    todo.completed = completed
    db.commit()
    db.refresh(todo)
    return todo


# Eliminar una tarea
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a specific todo item."""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(todo)
    db.commit()
    return {"ok": True}
