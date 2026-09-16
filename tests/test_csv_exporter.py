import csv
from datetime import datetime, timezone
from decimal import Decimal

from src.domain.models import Criptomoeda
from src.infrastructure.exporters.csv_exporter import CsvExporter


def test_exporta_csv_com_cabecalho_e_dados(tmp_path) -> None:
    moeda = Criptomoeda(
        posicao=1,
        nome="Bitcoin",
        simbolo="BTC",
        preco_usd=Decimal("75000.25"),
        variacao_24h=Decimal("2.5"),
        capitalizacao_usd=Decimal("1500000000000"),
        volume_24h_usd=Decimal("30000000000"),
        fonte="api",
        coletado_em=datetime(2026, 9, 16, 12, 0, tzinfo=timezone.utc),
    )

    destino = CsvExporter().exportar([moeda], tmp_path / "resultado.csv")

    with destino.open(encoding="utf-8-sig", newline="") as arquivo:
        linhas = list(csv.DictReader(arquivo))

    assert len(linhas) == 1
    assert linhas[0]["simbolo"] == "BTC"
    assert linhas[0]["preco_usd"] == "75000.25"
