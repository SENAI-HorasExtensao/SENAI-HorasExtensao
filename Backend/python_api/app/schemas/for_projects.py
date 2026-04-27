from pydantic import BaseModel
from typing import Optional

class ProjetoCreate(BaseModel):
    titulo: str
    descricao: str
    horas_previstas: int
    id_curso: str

class ProjetoRead(BaseModel):
    id: str        
    id_docente: str 
    titulo: str
    descricao: str
    horas_previstas: int
    id_curso: str

    class Config:
        from_attributes = True 

class ProjetoUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    horas_previstas: Optional[int] = None
    id_curso: Optional[str] = None        