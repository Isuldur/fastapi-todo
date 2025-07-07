"""Routes for the todo app."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Todo
from app.schemas import TodoCreate
from app.schemas import TodoUpdate


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
    todo: TodoCreate,
    db: Session = Depends(get_db)
):
    """Create a new todo item."""
    new_todo = Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


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
    updated_data: TodoUpdate,
    db: Session = Depends(get_db),
):
    """Update a specific todo item."""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    todo.title = updated_data.title
    todo.description = updated_data.description or ""
    todo.completed = updated_data.completed

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
