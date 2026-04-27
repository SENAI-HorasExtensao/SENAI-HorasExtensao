from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.for_projects import ProjetoCreate, ProjetoRead
from app.services import project_services as service
from app.schemas.for_projects import ProjetoUpdate

router = APIRouter(prefix="/projetos", tags=["Projetos"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def cadastrar(project_data: ProjetoCreate):
    # substituir pelo docente autenticado (login)
    id_docente = "TEMP_DOCENTE_ID"

    return service.cadastrar_projeto(project_data, id_docente)

@router.get("/", response_model=List[ProjetoRead])
def listar(id_curso: str = None):
    return service.listar_projetos(id_curso=id_curso)

@router.delete("/{id}")
def excluir(id: str):
    return service.excluir_projeto(id)

@router.put("/{id}")
def editar(id: str, project_data: ProjetoUpdate):
    resultado = service.editar_projeto(id, project_data)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return resultado    