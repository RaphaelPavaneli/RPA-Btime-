import argparse
import logging
from pathlib import Path
from typing import Any

from src.application.coletar_criptomoedas import coletar_e_exportar
from src.infrastructure.errors import ErroColeta
from src.infrastructure.exporters.csv_exporter import CsvExporter


def executar_cli(coletor: Any, nome_fonte: str, arquivo_padrao: str) -> int:
    parser = argparse.ArgumentParser(
        description=f"Coleta cotações da CoinLore por {nome_fonte} e gera um CSV."
    )
    parser.add_argument("--limite", type=int, default=100, help="Quantidade de moedas (1 a 100).")
    parser.add_argument(
        "--saida",
        type=Path,
        default=Path("output") / arquivo_padrao,
        help="Caminho do arquivo CSV.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        quantidade, arquivo = coletar_e_exportar(
            coletor=coletor,
            exportador=CsvExporter(),
            limite=args.limite,
            destino=args.saida,
        )
    except (ErroColeta, RuntimeError, ValueError, OSError) as exc:
        logging.error("Coleta não concluída: %s", exc)
        return 1

    logging.info("%s registros exportados para %s", quantidade, arquivo)
    return 0
