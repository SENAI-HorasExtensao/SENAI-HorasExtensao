from fastapi import FastAPI
from routes import auth, admin, aluno, docente, solicitacao_horas

app = FastAPI(title="SENAI Horas Extensão")

# Registrando as rotas padronizadas
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(aluno.router)
app.include_router(docente.router)
app.include_router(solicitacao_horas.router)

@app.get("/")
def home():
    return {"status": "Ativo", "documentacao": "/docs"}
