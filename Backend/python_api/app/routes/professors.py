from fastapi import APIRouter
from app.connection import get_db_connection

router = APIRouter(prefix="/professors", tags=["Professores"])

@router.get("/")
def list_professors():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT id, nome, especialidade FROM professores")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()