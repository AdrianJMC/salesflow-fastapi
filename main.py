from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Sale
from schemas import SaleCreate, SaleResponse
from builders.report_builder import ReportBuilder
from builders.invoice_builder import InvoiceBuilder

app = FastAPI(title="SalesFlow API", version="1.0")

@app.get("/")
def home():
    return {"message": "SalesFlow API funcionando 🚀"}

# Crear venta
@app.post("/sales", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

# Listar todas
@app.get("/sales", response_model=list[SaleResponse])
def list_sales(db: Session = Depends(get_db)):
    return db.query(Sale).all()

# Buscar por cliente
@app.get("/sales/client/{client_name}", response_model=list[SaleResponse])
def get_sales_by_client(client_name: str, db: Session = Depends(get_db)):
    results = db.query(Sale).filter(Sale.client.like(f"%{client_name}%")).all()
    if not results:
        raise HTTPException(status_code=404, detail="No se encontraron ventas para ese cliente")
    return results

# Generar reporte (usando Builder)
@app.get("/sales/report")
def generate_report(db: Session = Depends(get_db)):
    sales = db.query(Sale).all()
    report = ReportBuilder().with_sales(sales).add_summary().build()
    return report

# Generar factura (usando Builder)
@app.get("/sales/invoice/{sale_id}")
def generate_invoice(sale_id: int, db: Session = Depends(get_db)):
    sale = db.query(Sale).get(sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    invoice = InvoiceBuilder().for_sale(sale).with_tax(16).build()
    return invoice
