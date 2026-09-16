from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation

from requests import Session
from requests.exceptions import JSONDecodeError, RequestException

from src.domain.models import Criptomoeda
from src.infrastructure.errors import AcessoBloqueadoError, ErroColeta
from src.infrastructure.http import criar_sessao_http


class CoinLoreApiCollector:
    URL = "https://api.coinlore.net/api/tickers/"

    def __init__(self, session: Session | None = None, timeout: float = 20.0) -> None:
        self._session = session or criar_sessao_http()
        self._timeout = timeout

    def coletar(self, limite: int) -> list[Criptomoeda]:
        try:
            response = self._session.get(
                self.URL,
                params={"start": 0, "limit": limite},
                timeout=self._timeout,
            )
        except RequestException as exc:
            raise ErroColeta(f"Falha de comunicação com a API CoinLore: {exc}") from exc

        if response.status_code in (403, 429):
            raise AcessoBloqueadoError(
                f"A API CoinLore recusou ou limitou o acesso (HTTP {response.status_code}). "
                "Aguarde antes de tentar novamente."
            )
        try:
            response.raise_for_status()
            payload = response.json()
        except JSONDecodeError as exc:
            raise ErroColeta("A API CoinLore retornou um JSON inválido.") from exc
        except RequestException as exc:
            raise ErroColeta(f"A API CoinLore respondeu com erro: {exc}") from exc

        dados = payload.get("data") if isinstance(payload, dict) else None
        if not isinstance(dados, list):
            raise ErroColeta("A resposta da API CoinLore não contém a lista 'data'.")

        coletado_em = datetime.now(timezone.utc)
        resultado: list[Criptomoeda] = []
        for item in dados[:limite]:
            try:
                resultado.append(
                    Criptomoeda(
                        posicao=int(item["rank"]),
                        nome=str(item["name"]).strip(),
                        simbolo=str(item["symbol"]).strip().upper(),
                        preco_usd=Decimal(str(item["price_usd"])),
                        variacao_24h=Decimal(str(item["percent_change_24h"])),
                        capitalizacao_usd=Decimal(str(item["market_cap_usd"])),
                        volume_24h_usd=Decimal(str(item["volume24"])),
                        fonte="api",
                        coletado_em=coletado_em,
                    )
                )
            except (InvalidOperation, KeyError, TypeError, ValueError) as exc:
                raise ErroColeta(f"Registro inválido recebido da API CoinLore: {exc}") from exc

        return resultado
