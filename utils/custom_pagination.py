from fastapi import FastAPI, Query
from fastapi_pagination import Page, Params, add_pagination, paginate
from fastapi_pagination.customization import CustomizedPage, UseParams
from typing import TypeVar, Sequence
from pydantic import Field

T = TypeVar("T")


class MyCustomPage(Page[T]):
    items: Sequence[T] = Field(alias="itens")
    page: int = Field(title="Pagina", alias="pagina")
    size: int = Field(alias="totalRegistroPagina")
    pages: int = Field(alias="totalPaginas")


class MyCustomParams(Params):
    page: int = Query(default=1, description="Pagina", ge=1, alias="pagina")

    size: int = Query(
        default=10,
        description="Registros por Pagina",
        ge=1,
        le=100,
        alias="totalRegistroPagina",
    )


CustomPage = CustomizedPage[
    MyCustomPage[T],
    UseParams(MyCustomParams),
]
