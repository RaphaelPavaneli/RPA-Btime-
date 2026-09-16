import csv
from pathlib import Path
from typing import Sequence

from src.domain.models import Criptomoeda


class CsvExporter:
    CABECALHO = (
        "posicao",
        "nome",
        "simbolo",
        "preco_usd",
        "variacao_24h",
        "capitalizacao_usd",
        "volume_24h_usd",
        "fonte",
        "coletado_em",
    )

    def exportar(self, criptomoedas: Sequence[Criptomoeda], destino: Path) -> Path:
        destino.parent.mkdir(parents=True, exist_ok=True)
        temporario = destino.with_suffix(f"{destino.suffix}.tmp")

        try:
            with temporario.open("w", encoding="utf-8-sig", newline="") as arquivo:
                writer = csv.writer(arquivo)
                writer.writerow(self.CABECALHO)
                for moeda in criptomoedas:
                    writer.writerow(
                        (
                            moeda.posicao,
                            moeda.nome,
                            moeda.simbolo,
                            str(moeda.preco_usd),
                            str(moeda.variacao_24h),
                            str(moeda.capitalizacao_usd),
                            str(moeda.volume_24h_usd),
                            moeda.fonte,
                            moeda.coletado_em.isoformat(),
                        )
                    )
            temporario.replace(destino)
        finally:
            temporario.unlink(missing_ok=True)

        return destino.resolve()
