from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router, tags_metadata
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.0.1",
    description="Api de Serviço do Fornexpress",
    openapi_tags=tags_metadata,
)

add_pagination(app)
app.include_router(api_router, prefix=settings.API_V1_STR)

# Configurações de CORS
origins = [
    "http://localhost",  # Permitir frontend local
    # "http://localhost:5173",  # Permitir frontend no React (porta 5173)
    # "http://localhost:5174",  # Permitir frontend no React (porta 5174)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Domínios permitidos
    allow_credentials=True,  # Permitir envio de cookies
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
