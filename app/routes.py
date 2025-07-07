"""Routes for the todo app."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Todo


router = APIRouter()


def get_db():
    """Get database session dependency."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@router.get("/todos")
def get_all_todos(db: Session = Depends(get_db)):
    """Get all todo items."""
    return db.query(Todo).all()


@router.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a specific todo item by ID."""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return todo


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


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a specific todo item."""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(todo)
    db.commit()
    return {"ok": True}
