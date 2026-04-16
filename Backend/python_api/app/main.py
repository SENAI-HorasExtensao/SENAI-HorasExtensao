from fastapi import FastAPI
from app.routes import auth, admin, students, professors

app = FastAPI(title="SENAI Horas Extensão")

# Registrando as rotas padronizadas
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(students.router)
app.include_router(professors.router)

@app.get("/")
def home():
    return {"status": "Online", "documentacao": "/docs"}