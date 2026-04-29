from fastapi import APIRouter, HTTPException
from database.connection import get_db_connection
from app.services.auth_services import realizar_login_service
from app.schemas.for_users import LoginSchema

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/login")
def login(dados: LoginSchema):
    db = get_db_connection()
    try:
        return realizar_login_service(db, dados.cpf, dados.senha)
    finally:
        db.close()

@router.get("/perfil/{id}")
def obter_perfil(id: str): # str para aceitar UUID (CHAR 36)
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        query = """
            SELECT u.nome, u.email, u.cpf, t.nome as tipo_usuario 
            FROM usuario u
            INNER JOIN tipo_usuario t ON u.id_tipo_usuario = t.id
            WHERE u.id = %s
        """
        cursor.execute(query, (id,))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
            
        return user
    finally:
        cursor.close()
        db.close()