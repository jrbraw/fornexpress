from typing import Optional, List, TypeVar
from pydantic import Field, BaseModel as SCBaseModel
from datetime import datetime


class UsuarioSchema(SCBaseModel):

    id: Optional[int] = None
    nome: str
    email: str
    cpf: str
    cnpj: str
    senha: str
    foto_perfil: Optional[str] = None
    data_criacao: Optional[datetime] = None
    data_alteracao: Optional[datetime] = None

    class Config:
        from_attributes = True


class UsuariosSchemaGet(SCBaseModel):
    itens: List[UsuarioSchema]
    totalPaginas: int


class UsuariosSchemaPost(SCBaseModel):
    nome: str
    email: str
    cpf: str
    cnpj: str
    senha: str
