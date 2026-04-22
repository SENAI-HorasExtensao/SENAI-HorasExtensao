from pydantic import BaseModel

class SolicitacaoRequest(BaseModel):
    id_projeto: str
    id_aluno: str
    comprovante: str
    observacao_aluno: str | None = None
