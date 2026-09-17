# CryptoData — aplicação fullstack de criptomoedas

Aplicação desenvolvida como evolução do desafio técnico de RPA da Btime. A solução
original coleta dados de criptomoedas por API pública e web scraping e exporta os
resultados em CSV. Esta branch acrescenta uma API FastAPI e uma interface React para
consultar os dados e baixar os arquivos pelo navegador.

> Os dados são demonstrativos e não constituem recomendação financeira.

## Funcionalidades

- consulta de criptomoedas pela API pública da CoinLore;
- coleta dos mesmos dados por web scraping do site CoinLore;
- normalização das duas fontes em um único modelo;
- exibição dos resultados em uma interface web responsiva;
- download dos dados em CSV;
- tratamento de timeout, falhas temporárias, HTTP `403` e HTTP `429`;
- documentação interativa da API com Swagger.

## Tecnologias

### Backend

- Python 3.11;
- FastAPI e Uvicorn;
- Pydantic;
- Requests;
- Beautiful Soup.

### Frontend

- React 19;
- TypeScript;
- Vite;
- Tailwind CSS.

## Estrutura

```text
.
├── backend/
│   ├── scripts/             # Entradas de linha de comando
│   ├── src/
│   │   ├── api/             # Rotas e schemas HTTP
│   │   ├── application/     # Casos de uso
│   │   ├── domain/          # Modelo de domínio
│   │   └── infrastructure/  # Coletores HTTP e exportação CSV
│   └── output/              # CSVs gerados
└── frontend/
    └── src/
        ├── components/      # Componentes visuais
        ├── pages/           # Páginas da aplicação
        ├── services/        # Comunicação com o backend
        └── types/           # Tipos TypeScript
```

O backend aplica uma separação simples inspirada em Clean Architecture. A regra de
negócio não depende do FastAPI, do HTML, do JSON ou do formato CSV.

## Pré-requisitos

- Python 3.11 ou superior;
- Node.js `20.19` ou superior, ou `22.12` ou superior;
- npm;
- acesso à internet para consultar a CoinLore.

Para a execução em containers, Docker Desktop com Docker Compose substitui a
necessidade de instalar Python, Node.js e npm diretamente na máquina.

## Instalação do backend

No primeiro terminal, a partir da raiz do repositório:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Inicie a API:

```powershell
python -m uvicorn src.main:app --reload
```

A API ficará disponível em:

- aplicação: http://127.0.0.1:8000;
- Swagger: http://127.0.0.1:8000/docs;
- OpenAPI: http://127.0.0.1:8000/openapi.json.

## Instalação do frontend

Mantenha o backend em execução. Em outro terminal, a partir da raiz do repositório:

```powershell
cd frontend
npm ci
npm run dev
```

A interface ficará disponível em http://127.0.0.1:5173.

Durante o desenvolvimento, o Vite encaminha as requisições iniciadas por `/api` para
`http://127.0.0.1:8000`. Por isso, os dois serviços devem estar em execução.

## Executar com Docker

Com o Docker Desktop iniciado, execute na raiz do repositório:

```powershell
docker compose up --build
```

O Compose constrói e inicia dois serviços:

- `backend`: API FastAPI publicada na porta `8000`;
- `frontend`: build React servido pelo Nginx na porta `5173`.

Acesse:

- frontend: http://localhost:5173;
- backend: http://localhost:8000;
- Swagger: http://localhost:8000/docs.

No container, o Nginx encaminha `/api` para o serviço `backend`. Essa configuração
substitui o proxy do Vite usado pelo comando `npm run dev`.

Para acompanhar os logs:

```powershell
docker compose logs -f
```

Para encerrar e remover os containers e a rede criada pelo Compose:

```powershell
docker compose down
```

## Endpoints

| Método | Endpoint | Descrição |
| --- | --- | --- |
| `GET` | `/` | Verifica se a API está disponível |
| `GET` | `/api/criptomoedas?fonte=api&limite=10` | Consulta dados pela API pública |
| `GET` | `/api/criptomoedas?fonte=scraping&limite=10` | Consulta dados por web scraping |
| `GET` | `/api/criptomoedas/csv?fonte=api&limite=10` | Gera e baixa o CSV da API |
| `GET` | `/api/criptomoedas/csv?fonte=scraping&limite=10` | Gera e baixa o CSV do scraping |

O parâmetro `fonte` aceita `api` ou `scraping`, e `limite` aceita valores entre 1 e
100.

## Execução sem interface

Os scripts originais continuam disponíveis no backend:

```powershell
cd backend
python -m scripts.executar_api
python -m scripts.executar_scraping
```

É possível informar quantidade e arquivo de destino:

```powershell
python -m scripts.executar_api --limite 20 --saida output\api_20.csv
python -m scripts.executar_scraping --limite 20 --saida output\scraping_20.csv
```

## Verificações do frontend

```powershell
cd frontend
npm run lint
npm run build
```

## Limitações

- o scraping depende da estrutura HTML atual da CoinLore;
- a aplicação não tenta contornar CAPTCHA ou mecanismos de proteção;
- o proxy do Vite é destinado ao ambiente local de desenvolvimento;
- os CSVs gerados dentro do container não persistem após sua remoção;
- as cotações podem variar entre as duas coletas porque são obtidas em momentos
  diferentes.

## Fontes de dados

- site: https://www.coinlore.com/;
- documentação da API: https://www.coinlore.com/cryptocurrency-data-api.
