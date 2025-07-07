# 📝 FastAPI TODO API

Una API RESTful desarrollada con [FastAPI](https://fastapi.tiangolo.com/) para gestionar tareas (TODOs). Este proyecto forma parte de mi portafolio backend y está pensado para demostrar buenas prácticas, estructura limpia y pruebas automáticas.

---

## 🚀 Características

- CRUD completo de tareas
- Validación de datos con Pydantic
- Base de datos SQLite usando SQLAlchemy
- Pruebas automatizadas con Pytest
- Documentación interactiva con Swagger (OpenAPI)
- Estructura escalable y limpia

---

## 🛠️ Tecnologías

- Python 3.11+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Pytest
- HTTPX (para tests)

---

## 📦 Instalación

1. **Clona el repositorio**

git clone https://github.com/tu_usuario/fastapi-todo.git
cd fastapi-todo

3. **Crea y activa el entorno virtual**

python -m venv venv
venv\Scripts\activate  # En Windows
source venv/bin/activate  # En Mac/Linux

3. **Instala las dependencias**

pip install -r requirements.txt

4. **Ejecuta el servidor**

uvicorn main:app --reload

Adicional: **Correr las pruebas**

pytest

