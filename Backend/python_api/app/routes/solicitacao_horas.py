from fastapi import APIRouter
from datetime import datetime
from database.connection import get_db_connection
from schemas.solicitacao_horas import SolicitacaoRequest
import uuid

router = APIRouter(prefix="/solicitacoes", tags=["Solicitações"])

@router.post("")
def criar_solicitacao(data: SolicitacaoRequest):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO solicitacao_horas_aluno
        (id, id_projeto, status, id_aluno, data_postagem, comprovante, observacao_aluno)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            str(uuid.uuid4()),
            data.id_projeto,
            "Pendente",
            data.id_aluno,
            datetime.now(),
            data.comprovante,
            data.observacao_aluno
        )

        cursor.execute(query, values)
        conn.commit()

        return {"message": "Solicitação criada com sucesso"}

    except Exception as e:
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()
