from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.sale import Sale
from app.schemas.schemas import SaleCreate, SaleResponse
from app.builders.report_builder import ReportBuilder
from app.builders.invoice_builder import InvoiceBuilder

router = APIRouter(prefix="/sales", tags=["Sales"])

#Crear ventas
@router.post("/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    db_sale = Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

#Listar todas las ventas
@router.get("/", response_model=list[SaleResponse])
def list_sales(db: Session = Depends(get_db)):
    return db.query(Sale).all()

#buscar venta por cliente
@router.get("/client/{client_name}", response_model=list[SaleResponse])
def get_sales_by_client(client_name: str, db: Session = Depends(get_db)):
    results = db.query(Sale).filter(Sale.client.like(f"%{client_name}%")).all()
    if not results:
        raise HTTPException(status_code=404, detail="No se encontraron ventas para ese cliente")
    return results

#actualizar venta
@router.put("/sales/{sale_id}", response_model=SaleResponse)
def update_sale(sale_id: int, updated_sale: SaleCreate, db: Session = Depends(get_db)):
    sale = db.query(Sale).get(sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Venta no encontrada")

    for key, value in updated_sale.dict().items():
        setattr(sale, key, value)

    db.commit()
    db.refresh(sale)
    return sale

#eliminar venta
@router.delete("/sales/{sale_id}")
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = db.query(Sale).get(sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Venta no encontrada")

    db.delete(sale)
    db.commit()
    return {"message": f"Venta {sale_id} eliminada correctamente"}

#Generar reporte (Patrón Builder)
@router.get("/report")
def generate_report(db: Session = Depends(get_db)):
    sales = db.query(Sale).all()
    report = ReportBuilder().with_sales(sales).add_summary().build()
    return report

#Generar factura (Patrón Builder)
@router.get("/invoice/{sale_id}")
def generate_invoice(sale_id: int, db: Session = Depends(get_db)):
    sale = db.query(Sale).get(sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    invoice = InvoiceBuilder().for_sale(sale).with_tax(16).build()
    return invoice
