from pydantic import BaseModel
from typing import Optional

class ProjetoCreate(BaseModel):
    id_docente: str
    id_curso: str
    titulo: str
    descricao: str
    horas_previstas: int

class ProjetoRead(BaseModel):
    id: str
    id_docente: str 
    id_curso: str
    titulo: str
    descricao: str
    horas_previstas: int

    class Config:
        from_attributes = True

class ProjetoDelete(BaseModel):
    id: str

class ProjetoUpdate(BaseModel):
    id_docente: Optional[str] = None
    id_curso: Optional[str] = None        
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    horas_previstas: Optional[int] = None
