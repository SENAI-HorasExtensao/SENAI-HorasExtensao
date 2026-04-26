from fastapi import APIRouter, HTTPException
from app.database.connection import get_db_connection

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/login")
def login(dados: dict):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        # Exemplo de lógica de login
        cursor.execute("SELECT * FROM usuario WHERE email = %s", (dados['email'],))
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")
        return {"message": "Login realizado", "user": user['nome']}
    finally:
        cursor.close()
        db.close()
