from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation

from bs4 import BeautifulSoup
from requests import Session
from requests.exceptions import RequestException

from src.domain.models import Criptomoeda
from src.infrastructure.errors import AcessoBloqueadoError, ErroColeta
from src.infrastructure.http import criar_sessao_http


class CoinLoreScraper:
    URL = "https://www.coinlore.com/"

    def __init__(self, session: Session | None = None, timeout: float = 20.0) -> None:
        self._session = session or criar_sessao_http()
        self._timeout = timeout

    def coletar(self, limite: int) -> list[Criptomoeda]:
        try:
            response = self._session.get(self.URL, timeout=self._timeout)
        except RequestException as exc:
            raise ErroColeta(f"Falha de comunicação com o site CoinLore: {exc}") from exc

        if response.status_code in (403, 429):
            raise AcessoBloqueadoError(
                f"O site CoinLore recusou ou limitou o acesso (HTTP {response.status_code}). "
                "Aguarde antes de tentar novamente."
            )
        try:
            response.raise_for_status()
        except RequestException as exc:
            raise ErroColeta(f"O site CoinLore respondeu com erro: {exc}") from exc

        return self._extrair(response.text, limite)

    @staticmethod
    def _extrair(html: str, limite: int) -> list[Criptomoeda]:
        soup = BeautifulSoup(html, "html.parser")
        linhas = soup.select("tr[data-id]")
        if not linhas:
            raise ErroColeta("A tabela esperada não foi encontrada no HTML da CoinLore.")

        coletado_em = datetime.now(timezone.utc)
        resultado: list[Criptomoeda] = []

        for linha in linhas[:limite]:
            try:
                colunas = linha.find_all("td", recursive=False)
                nome_elemento = linha.select_one(".coin-symbol")
                simbolo_elemento = linha.select_one(".coin-name")
                preco_elemento = linha.select_one(".price_td_p [data-fiat]")
                variacao_elemento = linha.select_one(".h24_change[data-p]")
                capitalizacao_elemento = linha.select_one(".market-cap[data-fiat]")
                volume_elemento = linha.select_one(".table-volume-class[data-fiat]")

                if len(colunas) < 2 or not all(
                    (
                        nome_elemento,
                        simbolo_elemento,
                        preco_elemento,
                        variacao_elemento,
                        capitalizacao_elemento,
                        volume_elemento,
                    )
                ):
                    raise ValueError("campos obrigatórios ausentes")

                resultado.append(
                    Criptomoeda(
                        posicao=int(colunas[1].get_text(strip=True)),
                        nome=nome_elemento.get_text(" ", strip=True),
                        simbolo=simbolo_elemento.get_text(" ", strip=True).upper(),
                        preco_usd=Decimal(preco_elemento["data-fiat"]),
                        variacao_24h=Decimal(variacao_elemento["data-p"]),
                        capitalizacao_usd=Decimal(capitalizacao_elemento["data-fiat"]),
                        volume_24h_usd=Decimal(volume_elemento["data-fiat"]),
                        fonte="web_scraping",
                        coletado_em=coletado_em,
                    )
                )
            except (InvalidOperation, KeyError, TypeError, ValueError) as exc:
                identificador = linha.get("data-id", "desconhecido")
                raise ErroColeta(
                    f"Não foi possível interpretar a moeda '{identificador}' no HTML: {exc}"
                ) from exc

        return resultado
