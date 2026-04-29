from pydantic import BaseModel

class LoginSchema(BaseModel):
    cpf: str
    senha: str