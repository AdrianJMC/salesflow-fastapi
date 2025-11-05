from app.core.database import engine

try:
    conn = engine.connect()
    print("✅ Conexión a MySQL exitosa!")
    conn.close()
except Exception as e:
    print("❌ Error de conexión:", e)
