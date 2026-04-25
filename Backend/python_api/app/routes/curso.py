from fastapi import APIRouter, HTTPException
from app.schemas.curso import CursoCreate, CursoUpdate
from app.services import curso_services

router = APIRouter(prefix="/curso", tags=["Curso"])

@router.get("/")
def listar():
    return curso_services.listar_cursos()

@router.post("/")
def cadastrar(dados: CursoCreate):
    return curso_services.cadastrar_curso(dados)

@router.put("/{curso_id}")
def editar(curso_id: str, dados: CursoUpdate):
    resultado = curso_services.editar_curso(curso_id, dados)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return resultado