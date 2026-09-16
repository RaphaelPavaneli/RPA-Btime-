from src.cli import executar_cli
from src.infrastructure.collectors.coinlore_scraper import CoinLoreScraper


if __name__ == "__main__":
    raise SystemExit(
        executar_cli(CoinLoreScraper(), "web scraping", "criptomoedas_scraping.csv")
    )
