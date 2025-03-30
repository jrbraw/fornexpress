from fastapi import APIRouter

from api.v1.routes import usuario

tags_metadata = [
    {
        "name": "USUARIOS",
        "description": "Serviços de usuários.",
    },
]


api_router = APIRouter()

api_router.include_router(usuario.router, prefix="/usuarios", tags=["USUARIOS"])
