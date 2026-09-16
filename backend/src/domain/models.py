from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class Criptomoeda:
    """Representação comum dos dados obtidos por scraping e por API."""

    posicao: int
    nome: str
    simbolo: str
    preco_usd: Decimal
    variacao_24h: Decimal
    capitalizacao_usd: Decimal
    volume_24h_usd: Decimal
    fonte: str
    coletado_em: datetime

    def __post_init__(self) -> None:
        if self.posicao <= 0:
            raise ValueError("A posição deve ser maior que zero.")
        if not self.nome.strip() or not self.simbolo.strip():
            raise ValueError("Nome e símbolo são obrigatórios.")
        if self.preco_usd < 0 or self.capitalizacao_usd < 0 or self.volume_24h_usd < 0:
            raise ValueError("Valores financeiros não podem ser negativos.")

