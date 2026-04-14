from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException

def get_progresso_aluno(id_aluno: int, db: Session):

    # Busca aluno + carga horária do curso

    query_aluno = text("""
        SELECT
            u.id        AS id_aluno,
            u.nome,
            c.nome      AS nome_curso,
            c.carga_horas_extensao
        FROM usuario u
        JOIN curso c ON c.id = u.id_curso
        WHERE u.id = :id_aluno
    """)
    aluno = db.execute(query_aluno, {"id_aluno": id_aluno}).mappings().first()

    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    # Soma as horas validadas

    query_horas = text("""
        SELECT COALESCE(SUM(horas_homologadas), 0) AS horas_validadas
        FROM solicitacao_horas_aluno
        WHERE id_aluno = :id_aluno
          AND status = 'Validado'
    """)
    resultado = db.execute(query_horas, {"id_aluno": id_aluno}).mappings().first()

    horas_validadas = float(resultado["horas_validadas"])
    carga_total = float(aluno["carga_horas_extensao"] or 0)

    progresso = min((horas_validadas / carga_total) * 100, 100.0) if carga_total > 0 else 0.0

    # Retorna os dados

    return {
        "id_aluno": aluno["id_aluno"],
        "nome": aluno["nome"],
        "curso": aluno["nome_curso"],
        "horas_validadas": horas_validadas,
        "carga_horas_extensao": carga_total,
        "progresso_percentual": round(progresso, 2)
    }