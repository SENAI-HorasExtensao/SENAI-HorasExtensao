from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SolicitacaoHorasCreate(BaseModel):
    id_projeto: str
    status: str
    id_aluno: str
    data_postagem: datetime
    horas_homologadas: int
    comprovante: str
    observacao_aluno: str
    comentario_docente: str
    data_processamento: datetime

class SolicitacaoHorasRead(BaseModel):
    id: str
    id_projeto: str
    status: str
    id_aluno: str
    data_postagem: datetime
    horas_homologadas: int
    comprovante: str
    observacao_aluno: str
    comentario_docente: str
    data_processamento: datetime

    class Config:
        from_attributes = True
        
class SolicitacaoHorasReadFromId(BaseModel):
    id: str

    class Config:
        from_attributes = True

class SolicitacaoHorasDelete(BaseModel):
    id: str

class SolicitacaoHorasUpdate(BaseModel):
    id: str
    id_projeto: Optional[str] = None
    status: Optional[str] = None
    id_aluno: Optional[str] = None
    data_postagem: Optional[datetime] = None
    horas_homologadas: Optional[int] = None
    comprovante: Optional[str] = None
    observacao_aluno: Optional[str] = None
    comentario_docente: Optional[str] = None
    data_processamento: Optional[datetime] = None
