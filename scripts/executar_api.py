from src.cli import executar_cli
from src.infrastructure.collectors.coinlore_api import CoinLoreApiCollector


if __name__ == "__main__":
    raise SystemExit(executar_cli(CoinLoreApiCollector(), "API", "criptomoedas_api.csv"))
