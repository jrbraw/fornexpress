from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime, func
from core.configs import settings


class UsuarioModel(SQLModel, table=True):
    """
    Representa a class UsuarioModel
    """

    __tablename__: str = "usuarios"
    __table_args__: dict = {"schema": "fornexpress"}

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    cpf: str = Field(unique=True)
    cnpj: str = Field(unique=True)
    email: str = Field(unique=True)
    senha: str
    foto_perfil: Optional[str] = Field(default="default.png")
    data_criacao: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        ),
    )
    data_alteracao: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now(), nullable=True),
    )
