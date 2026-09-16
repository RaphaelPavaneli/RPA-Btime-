from fastapi import FastAPI

from src.api.routers.criptomoedas import router as criptomoedas_router


app = FastAPI(
    title="CryptoData API",
    description="API para coleta e consulta de dados de criptomoedas.",
    version="1.0.0",
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "CryptoData API está funcionando.",
    }


app.include_router(
    criptomoedas_router,
    prefix="/api",
)