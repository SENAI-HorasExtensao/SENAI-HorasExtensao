from pydantic import BaseModel
from datetime import date
from typing import Optional

class CursoCreate(BaseModel):
    titulo: str
    periodo_inicio: date
    periodo_fim: date
    carga_horas_extensao: Optional[int] = None

class CursoUpdate(BaseModel):
    titulo: Optional[str] = None
    periodo_inicio: Optional[date] = None
    periodo_fim: Optional[date] = None
    carga_horas_extensao: Optional[int] = None

class CursoResponse(BaseModel):
    id: str
    titulo: str
    periodo_inicio: date
    periodo_fim: date
    carga_horas_extensao: Optional[int]