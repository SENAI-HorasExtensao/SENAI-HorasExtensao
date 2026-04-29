from fastapi import APIRouter
from app.database.connection import get_db_connection

router = APIRouter(prefix="/docente", tags=["Docente"])

@router.get("/")
def get_docente():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, nome FROM usuario")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()
