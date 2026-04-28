from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SolicitacaoUpdateRequest(BaseModel):
    status: Optional[str] = None
    horas_homologadas: Optional[int] = None
    observacao_aluno: Optional[str] = None
    comentario_docente: Optional[str] = None

class SolicitacaoGetResponse(BaseModel):
    id: str
    status: str
    horas_homologadas: Optional[int] = None
    observacao_aluno: Optional[str] = None
    comentario_docente: Optional[str] = None

class SolicitacaoUpdateResponse(BaseModel):
    mensagem: str