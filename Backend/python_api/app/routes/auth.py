from fastapi import APIRouter, HTTPException
from database.connection import get_db_connection
from app.core.security import verificar_senha, criar_token_acesso
from app.schemas.for_users import LoginSchema

router = APIRouter(prefix="/auth", tags=["Autenticação"])

# TELA: Login
@router.post("/login")
def login(dados: LoginSchema):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        # Busca por CPF 
        query = "SELECT id_usuario, cpf, senha_hash, tipo_perfil FROM usuario WHERE cpf = %s"
        cursor.execute(query, (dados.cpf,))
        
        if not user or not verificar_senha(dados.senha, user['senha_hash']):
            raise HTTPException(status_code=401, detail="CPF ou Senha incorretos")
        
        # Cria o token com a role (Aluno/Docente)
        token = criar_token_acesso(dados={"sub": str(user['id_usuario']), "role": user['tipo_perfil']})
        
        return {
            "access_token": token,
            "role": user['tipo_perfil'],
            "nome": user['nome']
        }
    finally:
        cursor.close()
        db.close()

# TELAS: Perfil do Aluno e Perfil do Docente
@router.get("/perfil/{id_usuario}")
def obter_perfil(id_usuario: int):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT nome, email, cpf, tipo_perfil FROM usuario WHERE id_usuario = %s", (id_usuario,))
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return user
    finally:
        cursor.close()
        db.close()