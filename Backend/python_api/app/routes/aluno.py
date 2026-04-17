from fastapi import APIRouter
from database.connection import get_db_connection

router = APIRouter(prefix="/aluno", tags=["Aluno"])

@router.get("/")
def get_students():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM usuario where role='Aluno'")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()
