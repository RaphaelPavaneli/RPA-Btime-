from decimal import Decimal

from src.infrastructure.collectors.coinlore_api import CoinLoreApiCollector
from src.infrastructure.collectors.coinlore_scraper import CoinLoreScraper


HTML = """
<table><tbody><tr id="1" data-id="bitcoin">
  <td></td><td>1</td><td></td>
  <td><p class="coin-symbol">Bitcoin</p><p class="coin-name">BTC</p></td>
  <td></td>
  <td class="price_td_p"><div data-fiat="75000.25"></div></td>
  <td><div class="h24_change" data-p="2.50"></div></td>
  <td></td><td></td>
  <td class="market-cap" data-fiat="1500000000000"></td>
  <td><div class="table-volume-class" data-fiat="30000000000"></div></td>
</tr></tbody></table>
"""


def test_scraper_normaliza_html() -> None:
    moeda = CoinLoreScraper._extrair(HTML, limite=1)[0]

    assert moeda.nome == "Bitcoin"
    assert moeda.simbolo == "BTC"
    assert moeda.preco_usd == Decimal("75000.25")
    assert moeda.fonte == "web_scraping"


class FakeResponse:
    status_code = 200

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict:
        return {
            "data": [
                {
                    "rank": 1,
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "price_usd": "75000.25",
                    "percent_change_24h": "2.50",
                    "market_cap_usd": "1500000000000",
                    "volume24": 30000000000,
                }
            ]
        }


class FakeSession:
    def get(self, *args: object, **kwargs: object) -> FakeResponse:
        return FakeResponse()


def test_api_normaliza_json() -> None:
    coletor = CoinLoreApiCollector(session=FakeSession())  # type: ignore[arg-type]
    moeda = coletor.coletar(limite=1)[0]

    assert moeda.nome == "Bitcoin"
    assert moeda.volume_24h_usd == Decimal("30000000000")
    assert moeda.fonte == "api"
