# app/main.py
from fastapi import FastAPI
from app.routers import sales

app = FastAPI(title="SalesFlow API", version="1.0")
app.include_router(sales.router)

@app.get("/")
def home():
    return {"message": "SalesFlow API funcionando 🚀"}
