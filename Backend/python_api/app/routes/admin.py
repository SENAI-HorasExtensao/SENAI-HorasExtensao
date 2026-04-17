from fastapi import APIRouter
from database.connection import get_db_connection

router = APIRouter(prefix="/admin", tags=["Administração"])

@router.get("/horas/aluno")
def get_solicitacao_horas_aluno():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT count(*) as total FROM solicitacao_horas_aluno")
        return cursor.fetchone()
    finally:
        cursor.close()
        db.close()
