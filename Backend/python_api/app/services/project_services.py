from app.database.connection import get_db_connection
from fastapi import HTTPException, status

def listar_projetos(id_curso: str = None):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        if id_curso:
            cursor.execute("SELECT * FROM projeto WHERE id_curso = %s", (id_curso,))
        else:
            cursor.execute("SELECT * FROM projeto")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()

def cadastrar_projeto(dados, id_docente: str):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("""
            INSERT INTO projeto (id_docente, id_curso, titulo, descricao, horas_previstas)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_docente, dados.id_curso, dados.titulo, dados.descricao, dados.horas_previstas))
        db.commit()
        return {"message": "Projeto cadastrado com sucesso"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao cadastrar: {str(e)}")
    finally:
        cursor.close()
        db.close()

def excluir_projeto(projeto_id: str):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        # Verifica se o projeto existe
        cursor.execute("SELECT id FROM projeto WHERE id = %s", (projeto_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Projeto não encontrado.")

        # Validação de integridade (Regra: Não excluir se houver solicitações)
        cursor.execute("SELECT 1 FROM solicitacao_horas_aluno WHERE id_projeto = %s LIMIT 1", (projeto_id,))
        if cursor.fetchone():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Exclusão bloqueada: Este projeto possui solicitações vinculadas."
            )

        # Exclusão física
        cursor.execute("DELETE FROM projeto WHERE id = %s", (projeto_id,))
        db.commit()
        return {"message": "Projeto excluído com sucesso."}
    finally:
        cursor.close()
        db.close()

def editar_projeto(projeto_id: str, dados):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        # Busca o projeto atual para garantir que ele existe
        cursor.execute("SELECT * FROM projeto WHERE id = %s", (projeto_id,))
        projeto_atual = cursor.fetchone()
        
        if not projeto_atual:
            return None

        novo_titulo = dados.titulo or projeto_atual["titulo"]
        nova_descricao = dados.descricao or projeto_atual["descricao"]
        novas_horas = dados.horas_previstas if dados.horas_previstas is not None else projeto_atual["horas_previstas"]
        novo_curso = dados.id_curso or projeto_atual["id_curso"]

        # Executa a atualização no banco
        cursor.execute("""
            UPDATE projeto 
            SET titulo=%s, descricao=%s, horas_previstas=%s, id_curso=%s
            WHERE id = %s
        """, (novo_titulo, nova_descricao, novas_horas, novo_curso, projeto_id))
        
        db.commit()
        return {"message": "Projeto atualizado com sucesso"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar: {str(e)}")
    finally:
        cursor.close()
        db.close()        