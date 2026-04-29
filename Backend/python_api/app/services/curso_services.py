from app.database.connection import get_db_connection

def listar_cursos():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM curso")
        return cursor.fetchall()
    finally:
        cursor.close()
        db.close()

def cadastrar_curso(dados):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("""
            INSERT INTO curso (titulo, periodo_inicio, periodo_fim, carga_horas_extensao)
            VALUES (%s, %s, %s, %s)
        """, (dados.titulo, dados.periodo_inicio, dados.periodo_fim, dados.carga_horas_extensao))
        db.commit()
        return {"message": "Curso cadastrado com sucesso"}
    finally:
        cursor.close()
        db.close()

def editar_curso(curso_id: str, dados):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        # Busca curso existente
        cursor.execute("SELECT * FROM curso WHERE id = %s", (curso_id,))
        curso = cursor.fetchone()
        if not curso:
            return None
        # Atualiza só os campos enviados
        novo_titulo = dados.titulo or curso["titulo"]
        novo_inicio = dados.periodo_inicio or curso["periodo_inicio"]
        novo_fim = dados.periodo_fim or curso["periodo_fim"]
        novas_horas = dados.carga_horas_extensao if dados.carga_horas_extensao is not None else curso["carga_horas_extensao"]

        cursor.execute("""
            UPDATE curso SET titulo=%s, periodo_inicio=%s, periodo_fim=%s, carga_horas_extensao=%s
            WHERE id = %s
        """, (novo_titulo, novo_inicio, novo_fim, novas_horas, curso_id))
        db.commit()
        return {"message": "Curso atualizado"}
    finally:
        cursor.close()
        db.close()
