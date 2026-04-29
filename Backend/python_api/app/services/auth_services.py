from app.core.security import verificar_senha, criar_token_acesso
from fastapi import HTTPException

def realizar_login_service(db, cpf, senha):
    cursor = db.cursor(dictionary=True)
    try:
        # Query correta conforme o banco e o revisor
        query = """
            SELECT u.id, u.senha, t.nome as role 
            FROM usuario u
            INNER JOIN tipo_usuario t ON u.id_tipo_usuario = t.id
            WHERE u.cpf = %s
        """
        cursor.execute(query, (cpf,))
        user = cursor.fetchone()

        if not user or not verificar_senha(senha, user['senha']):
            raise HTTPException(status_code=401, detail="CPF ou Senha incorretos")

        # Gerar o token com UUID (id) e perfil (role)
        token = criar_token_acesso(dados={
            "sub": str(user['id']), 
            "role": user['role']
        })

        return {"access_token": token, "token_type": "bearer"}
    finally:
        cursor.close()