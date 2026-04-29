from app.database.connection import get_db_connection
from fastapi import HTTPException, status
from typing import List, Optional, Dict, Any
from app.schemas.for_solicitacao_horas import SolicitacaoHorasCreate, SolicitacaoHorasUpdate, SolicitacaoHorasDelete, SolicitacaoHorasReadFromId

def listar_qualquer_solicitacao_para_projeto(id: str):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    try:
        # Procura alguma solicitação de hora em curso para que seja deletado
        cursor.execute("SELECT id FROM solicitacao_horas_aluno WHERE id_projeto = %s LIMIT 1", (id,))
        return cursor.fetchone()
    except Exception as e:
        raise Exception(f"Erro ao listar: {str(e)}")
    finally:
        cursor.close()
        db.close()
