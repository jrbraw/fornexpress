from typing import List
from datetime import datetime
from fastapi import APIRouter, status, Depends, HTTPException, Response, Path, Query

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.usuario_model import UsuarioModel
from utils.custom_pagination import CustomPage
from core.deps import get_session


from fastapi_pagination.ext.sqlmodel import paginate

# from fastapi_pagination import paginate


from faker import Faker
import asyncio

router = APIRouter()


@router.post(
    "",
    summary="Cadastra Novo Usuário",
    status_code=status.HTTP_201_CREATED,
    response_model=UsuarioModel,
    response_description="OK",
)
async def post_usuario(usuario: UsuarioModel, db: AsyncSession = Depends(get_session)):
    """
    Cria um usuario com base nos dados fornecidos:
    - **nome**: Nome do usuario.
    - **cpf_responsavel**: Cpf do usuario:
    - **cpnj**: Cpf do usuario:
    - **email**: Email do usuario.
    - **senha**: Senha do usuario.

    (ver campos obrigatórios em schema)
    """

    # for _ in range(100):
    #     faker = Faker()
    #     dados = {
    #         "nome": faker.name(),
    #         "email": faker.email(),
    #         "cpf": str(faker.random_number(digits=11, fix_len=True)),
    #         "cnpj": str(faker.random_number(digits=14, fix_len=True)),
    #         "senha": str(faker.random_number(digits=8, fix_len=True)),
    #     }
    #     novo_usuario = UsuarioModel(**dados)
    #     db.add(novo_usuario)

    novo_usuario = UsuarioModel(**usuario.model_dump())
    db.add(novo_usuario)
    await db.commit()

    return novo_usuario


@router.get(
    "",
    summary="Listagem de Usuários",
    status_code=status.HTTP_200_OK,
    response_model=CustomPage[UsuarioModel],
    response_description="OK",
)
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    """
    Listagem de Usuários
    """
    async with db as session:
        query = select(UsuarioModel).order_by(UsuarioModel.id)
        lista_usuarios = await paginate(session, query)

    return lista_usuarios


@router.get(
    "/{usuario_id}",
    summary="Consulta Usuário",
    status_code=status.HTTP_200_OK,
    response_model=UsuarioModel,
    response_description="OK",
)
async def get_usuario(
    usuario_id: int = Path(description="ID do Usuário", ge=1),
    db: AsyncSession = Depends(get_session),
):
    """
    Consulta usuario com base no ID
    """
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario = result.scalar_one_or_none()

    if not usuario:
        raise HTTPException(
            detail="Usuario não encontrado", status_code=status.HTTP_404_NOT_FOUND
        )
    return usuario


@router.put(
    "/{usuario_id}",
    summary="Atualiza Usuário",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=UsuarioModel,
    response_description="OK",
)
async def put_usuario(
    usuario_id: int, usuario: UsuarioModel, db: AsyncSession = Depends(get_session)
):
    """
    Atualizar um usuario com base nos dados fornecidos:
    - **nome**: Nome do usuario.
    - **usuario**: Matricula do usuario.
    - **cpf**: Cpf do usuario:
    - **email**: Email do usuario.
    - **senha**: Senha do usuario.

    (ver campos obrigatórios em schema)
    """

    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_update = result.scalar_one_or_none()

        if not usuario_update:
            raise HTTPException(
                detail="Usuario não encontrado", status_code=status.HTTP_404_NOT_FOUND
            )

        usuario_update.nome = usuario.nome
        # usuario_update.foto_perfil = usuario.foto_perfil
        # usuario_update.data_alteracao = datetime.now()

        await session.commit()
        return usuario_update


@router.delete(
    "/{usuario_id}",
    summary="Deleta Usuário",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="OK",
)
async def delete_usuario(
    usuario_id: int = Path(description="ID do Usuário", ge=1),
    db: AsyncSession = Depends(get_session),
):
    """
    Deleta usuario com base no ID
    """
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_delete = result.scalar_one_or_none()

        if not usuario_delete:
            raise HTTPException(
                detail="Usuário não encontrado", status_code=status.HTTP_404_NOT_FOUND
            )

        await session.delete(usuario_delete)
        await session.commit()
