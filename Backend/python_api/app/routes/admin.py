from fastapi import APIRouter
from app.connection import get_db_connection

router = APIRouter(prefix="/admin", tags=["Administração"])

@router.get("/relatorios")
def get_reports():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT count(*) as total FROM horas_extensao")
        return cursor.fetchone()
    finally:
        cursor.close()
        db.close()