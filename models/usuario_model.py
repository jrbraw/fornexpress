from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from core.configs import settings


class UsuarioModel(settings.DBaseModel):
    """
    Representa a class UsuarioModel
    """

    __tablename__ = "usuarios"
    __table_args__ = {"schema": "fornexpress"}

    id: int = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nome: str = Column(String(100), nullable=False)
    cpf: str = Column(String(11), nullable=False, unique=True)
    cnpj: str = Column(String(14), nullable=False, unique=True)
    email: str = Column(String(50), nullable=False, unique=True)
    senha: str = Column(String(100), nullable=False)
    foto_perfil: str = Column(String(100), default="default.png", nullable=False)
    data_criacao: datetime = Column(DateTime(timezone=True), server_default=func.now())
    data_alteracao: datetime = Column(DateTime(timezone=True), onupdate=func.now())
