# CryptoData — backend

Backend responsável por coletar e normalizar cotações de criptomoedas. Os dados podem
ser obtidos pela API pública da CoinLore ou por web scraping do site. A aplicação
disponibiliza uma API FastAPI, scripts de linha de comando e exportação em CSV.

> Os dados são demonstrativos e não constituem recomendação financeira.

## Dados coletados

- posição no ranking;
- nome e símbolo;
- preço em dólar;
- variação nas últimas 24 horas;
- capitalização de mercado;
- volume nas últimas 24 horas;
- fonte e horário da coleta.

## Arquitetura

O backend usa uma separação simples inspirada em Clean Architecture:

```text
API e scripts → application → domain
      ↓              ↑
 infrastructure ─────┘
```

- `domain`: modelo independente de frameworks e fontes externas;
- `application`: coordena os casos de uso;
- `infrastructure/collectors`: interpreta HTML ou JSON;
- `infrastructure/exporters`: grava os dados em CSV;
- `api`: expõe as operações por HTTP e valida as respostas;
- `scripts`: pontos de entrada para execução pelo terminal.

## Pré-requisitos

- Python 3.11 ou superior;
- acesso à internet para executar as coletas.

## Instalação

Execute os comandos dentro da pasta `backend`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Executar a API

```powershell
python -m uvicorn src.main:app --reload
```

A API ficará disponível em:

- aplicação: http://127.0.0.1:8000;
- Swagger: http://127.0.0.1:8000/docs;
- OpenAPI: http://127.0.0.1:8000/openapi.json.

### Endpoints

| Método | Endpoint | Descrição |
| --- | --- | --- |
| `GET` | `/` | Verifica a disponibilidade da API |
| `GET` | `/api/criptomoedas` | Consulta criptomoedas pela fonte informada |
| `GET` | `/api/criptomoedas/csv` | Coleta os dados e retorna um arquivo CSV |

Exemplos:

```text
GET /api/criptomoedas?fonte=api&limite=10
GET /api/criptomoedas?fonte=scraping&limite=10
GET /api/criptomoedas/csv?fonte=api&limite=10
```

O parâmetro `fonte` aceita `api` ou `scraping`, e `limite` aceita valores entre 1 e
100.

## Executar sem a API

Os coletores também podem ser executados diretamente pelo terminal:

```powershell
python -m scripts.executar_scraping
python -m scripts.executar_api
```

Por padrão, cada comando coleta 100 moedas. É possível alterar a quantidade e o
destino:

```powershell
python -m scripts.executar_scraping --limite 20 --saida output\scraping_20.csv
python -m scripts.executar_api --limite 20 --saida output\api_20.csv
```

## Arquivos gerados

```text
output/criptomoedas_scraping.csv
output/criptomoedas_api.csv
```

Os valores dos dois arquivos podem ser diferentes porque as cotações são obtidas em
momentos distintos. A coluna `coletado_em` registra o horário em UTC.

## Robustez e limitações

- requisições usam timeout;
- falhas temporárias e HTTP `429` usam novas tentativas com espera progressiva;
- o cabeçalho `Retry-After` é respeitado;
- respostas `403`, JSON inválido e mudanças no HTML geram mensagens claras;
- a gravação do CSV usa arquivo temporário para evitar resultado incompleto;
- o acesso é de baixo volume e não tenta contornar CAPTCHA ou proteções.

O scraping depende da estrutura HTML do site. Caso a CoinLore altere suas classes ou
atributos, o coletor precisará ser atualizado. A API tende a ser mais estável porque
possui um contrato documentado.

## Fontes

- site: https://www.coinlore.com/;
- documentação da API: https://www.coinlore.com/cryptocurrency-data-api.

Para executar também a interface React, consulte o `README.md` na raiz do
repositório.
