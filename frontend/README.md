# CryptoData — frontend

Interface web da aplicação CryptoData. O frontend permite escolher a fonte de coleta,
consultar criptomoedas e baixar o resultado em CSV.

## Tecnologias

- React 19;
- TypeScript;
- Vite;
- Tailwind CSS;
- ESLint.

## Pré-requisitos

- Node.js `20.19` ou superior, ou `22.12` ou superior;
- npm;
- backend em execução em `http://127.0.0.1:8000`.

## Instalação

Execute os comandos dentro da pasta `frontend`:

```powershell
npm ci
```

O comando `npm ci` utiliza as versões registradas no `package-lock.json`, oferecendo
uma instalação reproduzível.

## Executar em desenvolvimento

```powershell
npm run dev
```

Acesse http://127.0.0.1:5173.

O frontend envia requisições para caminhos iniciados por `/api`. Durante o
desenvolvimento, o proxy configurado no Vite encaminha essas requisições para
`http://127.0.0.1:8000`.

## Funcionalidades

- seleção entre API pública e web scraping;
- consulta das 10 primeiras criptomoedas;
- apresentação de carregamento, resultado vazio e falha;
- tabela responsiva com os dados normalizados;
- download do CSV correspondente à fonte selecionada.

## Estrutura principal

```text
src/
├── components/  # Componentes reutilizáveis da interface
├── pages/       # Composição das páginas
├── services/    # Requisições para o backend
├── types/       # Contratos TypeScript
├── App.tsx
└── main.tsx
```

O módulo `services/cryptoService.ts` concentra a comunicação HTTP. Os componentes
visuais não precisam conhecer os detalhes dos endpoints do backend.

## Comandos disponíveis

```powershell
npm run dev      # inicia o servidor de desenvolvimento
npm run lint     # executa a análise estática
npm run build    # valida o TypeScript e gera o build
npm run preview  # visualiza localmente o build gerado
```

## Integração com o backend

| Ação | Requisição |
| --- | --- |
| Consultar pela API | `GET /api/criptomoedas?fonte=api&limite=10` |
| Consultar por scraping | `GET /api/criptomoedas?fonte=scraping&limite=10` |
| Baixar CSV | `GET /api/criptomoedas/csv?fonte=<fonte>&limite=10` |

Para executar a aplicação completa, consulte o `README.md` na raiz do repositório.

## Limitações

- o proxy atual é destinado ao desenvolvimento local;
- o frontend depende do backend para consultar e exportar dados;
- não há persistência local: uma nova consulta substitui os dados exibidos.
