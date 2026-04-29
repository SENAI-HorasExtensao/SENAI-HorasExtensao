from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "SENAI_2026"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha(senha_plana, senha_do_banco):
    # Compara a senha digitada com o hash da coluna 'senha'
    return pwd_context.verify(senha_plana, senha_do_banco)

def criar_token_acesso(dados: dict):
    para_codificar = dados.copy()
    expira = datetime.utcnow() + timedelta(minutes=480) # 8 horas
    para_codificar.update({"exp": expira})
    return jwt.encode(para_codificar, SECRET_KEY, algorithm=ALGORITHM)