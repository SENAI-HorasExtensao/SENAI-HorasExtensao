from fastapi import APIRouter, HTTPException
from app.services import assessment_services as service

router = APIRouter(prefix="/solicitacoes", tags=["Avaliações de solicitações"])

# TODO: trocar response_model para schema de response
@router.get("/pendentes", response_model=object)
async def get_pendings():
    return service.get_pending_assessments()


# TODO: trocar response_model para schema de response
# TODO: trocar campos solicitados para schema de request 
@router.put("/{id}/avaliar", response_model=object)
async def update_assessment(id: int, new_status: str, hours_homologated: int, comment: str):
    resultado = service.update_assessment_status(id, new_status, hours_homologated, comment)

    if not resultado:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada no sistema.")
        
    return resultado