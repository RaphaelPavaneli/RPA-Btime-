class ErroColeta(RuntimeError):
    """Falha tratada durante a comunicação ou leitura de uma fonte externa."""


class AcessoBloqueadoError(ErroColeta):
    """A fonte recusou ou limitou temporariamente o acesso."""

