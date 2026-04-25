from sqlalchemy import Column, String, Integer, ForeignKey, Text
from app.database.connection import Base 
import uuid

class Projeto(Base):
    __tablename__ = "projeto"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_docente = Column(String(36), ForeignKey("usuario.id"), nullable=False)
    id_curso = Column(String(36), ForeignKey("curso.id"), nullable=False)
    titulo = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=False)
    horas_previstas = Column(Integer, nullable=True)