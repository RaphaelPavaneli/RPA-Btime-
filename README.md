# RPA Btime — Coleta de criptomoedas

Projeto desenvolvido para comparar duas formas de coleta de cotações de criptomoedas:

1. **Web scraping:** leitura da tabela pública do site CoinLore.
2. **API REST:** consumo da API pública da CoinLore.

Os dois fluxos normalizam os dados no mesmo modelo e geram arquivos CSV com estrutura idêntica.

> As cotações são apenas dados demonstrativos e não constituem recomendação financeira.

## Dados coletados

- posição no ranking;
- nome e símbolo;
- preço em dólar;
- variação nas últimas 24 horas;
- capitalização de mercado;
- volume nas últimas 24 horas;
- fonte e horário da coleta.

## Arquitetura

O projeto usa uma separação simples inspirada em Clean Architecture:

```text
scripts → application → domain
   ↓           ↑
infrastructure
```

- `domain`: modelo independente de frameworks e fontes externas;
- `application`: coordena o caso de uso;
- `infrastructure/collectors`: interpreta HTML ou JSON;
- `infrastructure/exporters`: grava os dados em CSV;
- `scripts`: pontos de entrada para o usuário;
- `tests`: valida a normalização e a exportação sem depender da internet.

## Pré-requisitos

- Python 3.11 ou superior;
- acesso à internet para executar as coletas.

## Instalação no Windows PowerShell

```powershell
cd "C:\Projetos\RPA - Btime"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Executar o web scraping

```powershell
python -m scripts.executar_scraping
```

## Executar a coleta pela API

```powershell
python -m scripts.executar_api
```

Por padrão, cada comando coleta 10 moedas. É possível alterar a quantidade e o destino:

```powershell
python -m scripts.executar_scraping --limite 20 --saida output\scraping_20.csv
python -m scripts.executar_api --limite 20 --saida output\api_20.csv
```

O limite aceito é de 1 a 100 moedas.

## Arquivos gerados

```text
output/criptomoedas_scraping.csv
output/criptomoedas_api.csv
```

As cotações variam continuamente. Por isso, os valores dos dois arquivos podem ser ligeiramente diferentes mesmo quando os comandos são executados em sequência. A coluna `coletado_em` registra o momento de cada coleta em UTC.

## Executar os testes

```powershell
python -m pytest
```

Os testes utilizam HTML e JSON controlados. Assim, verificam a interpretação dos dados sem ficarem instáveis quando a internet ou o serviço externo estiverem indisponíveis.

## Robustez e limitações

- requisições usam timeout;
- falhas temporárias e HTTP `429` usam novas tentativas com espera progressiva;
- o cabeçalho `Retry-After` é respeitado;
- respostas `403`, JSON inválido e mudanças no HTML geram mensagens claras;
- a gravação do CSV usa arquivo temporário para evitar resultado incompleto;
- o acesso é de baixo volume e não tenta contornar CAPTCHA ou mecanismos de proteção.

O scraping depende da estrutura HTML do site. Caso a CoinLore altere suas classes ou atributos, o coletor precisará ser atualizado. A API tende a ser mais estável porque possui contrato documentado.

## Fontes

- Site: https://www.coinlore.com/
- Documentação da API: https://www.coinlore.com/cryptocurrency-data-api

