from datetime import datetime
from database.connection import get_db_connection
from schemas.for_solicitacao_update import SolicitacaoUpdateRequest

# Cristian - Sem DB_Fake, busca direta do DB, mas com esta correção citada pendente
def get_solicitacao_horas_por_status(status:str):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM solicitacao_horas_aluno where status=%s", (status,))
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()


def update_status_solicitacao_horas(id_solicitacao_horas:str, solicitacao_update:SolicitacaoUpdateRequest):
    db = get_db_connection()
    cursor = db.cursor(dictionary=False)
    data_hora_agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:  
        cursor.execute("UPDATE solicitacao_horas_aluno set status=%s, horas_homologadas=%s, observacao_aluno=%s, comentario_docente=%s, data_processamento=%s where id=%s", (solicitacao_update.status, solicitacao_update.horas_homologadas, solicitacao_update.observacao_aluno, solicitacao_update.comentario_docente, data_hora_agora, id_solicitacao_horas))
        db.commit()
        return { "mensagem": "Solicitação de Horas atualizada com sucesso" }
    finally:
        cursor.close()
        db.close()
