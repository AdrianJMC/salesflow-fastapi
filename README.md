# 💼 SalesFlow – Gestor de Ventas (API REST + Patrón Builder)

Sistema desarrollado en **FastAPI + MySQL**, diseñado para la gestión de ventas, generación de facturas y reportes dinámicos.  
Aplica el **patrón de diseño Builder** para la creación flexible de documentos y demuestra una arquitectura **RESTful modular y escalable**.

---

## 🚀 Tecnologías utilizadas

- **FastAPI** → Framework backend principal  
- **MySQL** → Base de datos relacional  
- **SQLAlchemy** → ORM para la conexión con la BD  
- **Pydantic** → Validación de datos  
- **Uvicorn** → Servidor ASGI para ejecutar la API  
- **Python-dotenv** → Manejo de variables de entorno  
- **Git / GitHub** → Control de versiones

---

## 📁 Estructura del proyecto
GESTOR-VENTAS/
│
├── app/
│ ├── main.py # Archivo principal (punto de entrada)
│ ├── core/
│ │ └── database.py # Configuración de conexión a la BD
│ ├── models/
│ │ └── sale.py # Modelo de tabla 'sales'
│ ├── schemas/
│ │ └── schemas.py # Validación con Pydantic
│ ├── routers/
│ │ └── sales.py # Endpoints principales
│ ├── builders/
│ │ ├── report_builder.py # Generador de reportes (Builder)
│ │ └── invoice_builder.py # Generador de facturas (Builder)
│
├── tests/
│ └── test_db.py # Script para probar la conexión
│
├── create_tables.py # Crea tablas en la BD
├── .env # Variables de entorno (no se sube al repo)
├── .gitignore # Archivos ignorados en Git
└── README.md # Documentación del proyecto

---

## ⚙️ Configuración del entorno

### 1️⃣ Crear y activar entorno virtual

python -m venv venv
venv\Scripts\activate    # En Windows
# o en Linux/Mac:
# source venv/bin/activate

### 2️⃣ Instalar dependencias
pip install fastapi uvicorn pymysql sqlalchemy python-dotenv

## ⚙️ Configuración del entorno

### Crear tu propio archivo .env
# Variables de entorno para SalesFlow
DB_HOST=localhost
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=salesflow

## Crear la base de datos y tablas
### abre tu Mysql y ejecuta:
Create table salesflow;

### Luego en la terminal del proyecto ejecutar:
python create_tables.py

## ▶️ Ejecutar el servidor FastAPI
uvicorn app.main:app --reload

