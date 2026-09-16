from fastapi import APIRouter, HTTPException, Query

from src.application.coletar_criptomoedas import coletar_criptomoedas
from src.infrastructure.collectors.coinlore_api import CoinLoreApiCollector
from src.infrastructure.collectors.coinlore_scraper import CoinLoreScraper
from src.api.schemas.criptomoeda import CriptomoedaResponse


router = APIRouter(
    prefix="/criptomoedas",
    tags=["Criptomoedas"],
)


@router.get("", response_model=list[CriptomoedaResponse],)
def listar_criptomoedas(
    fonte: str = Query(default="api"),
    limite: int = Query(default=10, ge=1, le=100),
):
    try:
        if fonte == "api":
            coletor = CoinLoreApiCollector()

        elif fonte == "scraping":
            coletor = CoinLoreScraper()

        else:
            raise HTTPException(
                status_code=400,
                detail="Fonte inválida. Use 'api' ou 'scraping'.",
            )

        criptomoedas = coletar_criptomoedas(
            coletor=coletor,
            limite=limite,
        )

        return criptomoedas

    except ValueError as erro:
        raise HTTPException(
            status_code=400,
            detail=str(erro),
        ) from erro

    except RuntimeError as erro:
        raise HTTPException(
            status_code=502,
            detail=str(erro),
        ) from erro