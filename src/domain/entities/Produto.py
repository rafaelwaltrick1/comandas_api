# Rafael Waltrick
from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    valor: float
    foto: bytes = None