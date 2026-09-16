from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse

from pathlib import Path

from src.application.coletar_criptomoedas import coletar_criptomoedas, coletar_e_exportar
from src.infrastructure.collectors.coinlore_api import CoinLoreApiCollector
from src.infrastructure.collectors.coinlore_scraper import CoinLoreScraper
from src.api.schemas.criptomoeda import CriptomoedaResponse
from src.infrastructure.exporters.csv_exporter import CsvExporter



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


@router.get("/csv")
def baixar_csv(
    fonte: str = Query(default="api"),
    limite: int = Query(default=10, ge=1, le=100),
):
    if fonte == "api":
        coletor = CoinLoreApiCollector()
        nome_arquivo = "criptomoedas_api.csv"

    elif fonte == "scraping":
        coletor = CoinLoreScraper()
        nome_arquivo = "criptomoedas_scraping.csv"

    else:
        raise HTTPException(
            status_code=400,
            detail="Fonte inválida.",
        )

    destino = Path("output") / nome_arquivo

    exportador = CsvExporter()

    coletar_e_exportar(
        coletor=coletor,
        exportador=exportador,
        limite=limite,
        destino=destino,
    )

    return FileResponse(
        path=destino,
        media_type="text/csv",
        filename=nome_arquivo,
    )