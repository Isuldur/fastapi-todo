"""FastAPI application entry point."""
from fastapi import FastAPI
from database import engine
from models import Base
from routes import router  # 👈 importar las rutas

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)  # 👈 montar las rutas
