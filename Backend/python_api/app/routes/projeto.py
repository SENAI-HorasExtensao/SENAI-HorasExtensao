from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.for_projecto import ProjetoCreate, ProjetoRead, ProjetoUpdate
from app.services import projeto_services as service
from app.services import solicitacao_horas_services as sh_service

router = APIRouter(prefix="/projeto", tags=["Projeto"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def cadastrar(project_data: ProjetoCreate):
    try:
        # TODO: Validação do id do docente em autorização
        return service.cadastrar_projeto(project_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail="O projeto não pôde ser cadastrado")

@router.get("/{id}", response_model=ProjetoRead)
def listar_por_id(id: str = None):
    try:
        return service.listar_projeto_por_id(id=id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="O projeto não foi encontrado")

@router.get("/curso/{id_curso}", response_model=List[ProjetoRead])
def listar(id_curso: str = None):
    try:
        return service.listar_projetos(id_curso=id_curso)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Nenhum projeto encontrado para este curso")

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def excluir(id: str = None):
    # TODO: Validação da autorização para excluir
    
    # Verifica se o projeto pode ser encontrado
    try:
        projeto_por_id = service.listar_projeto_por_id(id=id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")

    # Se sim, verifica-se se ele pode ser encontrado nas solicitações de horas
    if sh_service.listar_qualquer_solicitacao_para_projeto(id) is not None:
        raise HTTPException(status_code=400, detail="Existe uma solitação de horas pendente para este projeto e não pode ser excluído até que se resolva.")
    else:
        try:
            return service.excluir_projeto(id) # Retorno em caso de sucesso
        except Exception as e:
            raise HTTPException(status_code=500, detail="O projeto não pôde ser excluído")

@router.put("/{id}", status_code=status.HTTP_200_OK)
def editar(id:str, project_data: ProjetoUpdate):
    try:
        # TODO: Validação da autorização para editar
        return service.editar_projeto(id, project_data)
    except Exception as e:
        raise HTTPException(status_code=404, detail="O projeto não pôde ser editado")
