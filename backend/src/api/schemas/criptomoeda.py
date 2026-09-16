from datetime import datetime

from pydantic import BaseModel


class CriptomoedaResponse(BaseModel):
    posicao: int
    nome: str
    simbolo: str
    preco_usd: float
    variacao_24h: float
    capitalizacao_usd: float
    volume_24h_usd: float
    fonte: str
    coletado_em: datetime