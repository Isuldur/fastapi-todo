"""Pydantic schemas for the todo application."""
from pydantic import BaseModel


class TodoBase(BaseModel):
    """Base Pydantic model for todo items."""
    title: str
    description: str | None = None


class TodoCreate(TodoBase):
    """Pydantic model for creating todo items."""


class TodoUpdate(TodoBase):
    """Pydantic model for updating todo items."""
    completed: bool


class TodoResponse(TodoBase):
    """Pydantic model for todo item responses."""
    id: int
    completed: bool

    class Config:
        """Pydantic configuration for ORM mode."""
        orm_mode = True
