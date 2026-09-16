from pathlib import Path
from typing import Protocol, Sequence

from src.domain.models import Criptomoeda


class ColetorCriptomoedas(Protocol):
    def coletar(self, limite: int) -> list[Criptomoeda]: ...


class ExportadorCriptomoedas(Protocol):
    def exportar(self, criptomoedas: Sequence[Criptomoeda], destino: Path) -> Path: ...


def coletar_e_exportar(
    coletor: ColetorCriptomoedas,
    exportador: ExportadorCriptomoedas,
    limite: int,
    destino: Path,
) -> tuple[int, Path]:
    """Coordena a coleta e a exportação sem conhecer HTML, JSON ou CSV."""

    if not 1 <= limite <= 100:
        raise ValueError("O limite deve estar entre 1 e 100.")

    criptomoedas = coletor.coletar(limite)
    if not criptomoedas:
        raise RuntimeError("A fonte não retornou nenhuma criptomoeda válida.")

    arquivo = exportador.exportar(criptomoedas, destino)
    return len(criptomoedas), arquivo
