from fastapi import FastAPI
from app.routes import auth, admin, aluno, docente, curso, projects

app = FastAPI(title="SENAI Horas Extensão")

# Registrando as rotas padronizadas
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(aluno.router)
app.include_router(docente.router)
app.include_router(curso.router)
app.include_router(projects.router)

@app.get("/")
def home():
    return {"status": "Ativo", "documentacao": "/docs"}
