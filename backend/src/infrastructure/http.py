from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


USER_AGENT = "RPA-Btime-Entrevista/1.0 (projeto educacional; contato via repositorio GitHub)"


def criar_sessao_http() -> Session:
    """Cria uma sessão com política conservadora para falhas temporárias."""

    retry = Retry(
        total=3,
        connect=3,
        read=3,
        status=3,
        backoff_factor=0.8,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    session = Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/json"})
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session
