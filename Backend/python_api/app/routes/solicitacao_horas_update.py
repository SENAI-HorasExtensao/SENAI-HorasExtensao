from fastapi import APIRouter, HTTPException
from schemas.for_solicitacao_update import SolicitacaoGetResponse, SolicitacaoUpdate, SolicitacaoUpdateResponse
from services import solicitacao_horas_services as service

router = APIRouter(prefix="/solicitacao_horas", tags=["horas"])

@router.get("/{status}", response_model=list[SolicitacaoGetResponse])
async def get_solicitacoes_por_status(status:str):
    return service.get_solicitacao_horas_por_status(status)


@router.put("/{id}", response_model=SolicitacaoUpdateResponse)
async def update_solicitacao_horas(id:str, solicitacao_update:SolicitacaoUpdate):
    resultado = service.update_status_solicitacao_horas(id, solicitacao_update)

    if not resultado:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada no sistema.")
        
    return resultado
