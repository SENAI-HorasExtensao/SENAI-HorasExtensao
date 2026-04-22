from datetime import datetime

DB_FAKE = [
    {
        "id": 1,
        "id_aluno": 10, 
        "id_projeto": 100, 
        "status": "Pendente",
        "comprovante_url": "http://link.com/doc1.pdf", 
        "comentario_docente": None,
        "horas_homologadas": 0,
        "data_processamento": datetime.now()
    },
    {
        "id": 2, 
        "id_aluno": 11, 
        "id_projeto": 101, 
        "status": "Pendente",
        "comprovante_url": "http://link.com/doc2.pdf", 
        "comentario_docente": None,
        "horas_homologadas": 0,
        "data_processamento": datetime.now()
    }
]


# TODO: trocar de DB_FAKE para o banco de dados real (model da dupla 4)
def get_pending_assessments():
    return [assessment for assessment in DB_FAKE if assessment["status"] == "Pendente"]; 


# TODO: trocar de DB_FAKE para o banco de dados real (model da dupla 4)
# TODO: trocar campos solicitados para schema de request 
def update_assessment_status(assessment_id: int, new_status: str, hours_homologated: int, comment: str):

    for assessment in DB_FAKE:
        if assessment["id"] == assessment_id:

            assessment["status"] = new_status
            assessment["horas_homologadas"] = hours_homologated
            assessment["comentario_docente"] = comment

            return assessment

    return None