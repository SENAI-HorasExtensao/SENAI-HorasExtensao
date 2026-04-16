from fastapi import APIRouter
from app.connection import get_db_connection

router = APIRouter(prefix="/students", tags=["Alunos"])

@router.get("/")
def get_students():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM alunos")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()