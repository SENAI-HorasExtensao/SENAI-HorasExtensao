from pydantic import BaseModel
from typing import Optional

class ProjetoBase(BaseModel):
    titulo: str
    descricao: str
    horas_previstas: int
    id_curso: str  

class ProjetoCreate(ProjetoBase):
    pass  

class ProjetoRead(ProjetoBase):
    id: str        
    id_docente: str 

    class Config:
        from_attributes = True 