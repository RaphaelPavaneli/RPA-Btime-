from fastapi import FastAPI

from src.api.routers.criptomoedas import router as criptomoedas_router


def create_app() -> FastAPI:
    """Cria e configura a aplicação FastAPI."""

    application = FastAPI(
        title="CryptoData API",
        version="1.0.0",
        description="API para consulta e coleta de dados de criptomoedas.",
    )

    @application.get("/")
    def health_check():
        return {
            "status": "ok",
            "message": "CryptoData API está funcionando.",
        }

    application.include_router(
        criptomoedas_router,
        prefix="/api",
    )

    return application


app = create_app()