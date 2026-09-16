import type { Criptomoeda } from "../types/crypto";

export const criptomoedasMock: Criptomoeda[] = [
  {
    posicao: 1,
    nome: "Bitcoin",
    simbolo: "BTC",
    preco_usd: 115230.45,
    variacao_24h: 2.41,
    capitalizacao_usd: 2290000000000,
    volume_24h_usd: 51200000000,
    fonte: "api",
    coletado_em: "2026-09-16T16:30:00",
  },
  {
    posicao: 2,
    nome: "Ethereum",
    simbolo: "ETH",
    preco_usd: 4510.32,
    variacao_24h: 1.08,
    capitalizacao_usd: 544000000000,
    volume_24h_usd: 27800000000,
    fonte: "api",
    coletado_em: "2026-09-16T16:30:00",
  },
  {
    posicao: 3,
    nome: "XRP",
    simbolo: "XRP",
    preco_usd: 3.02,
    variacao_24h: -0.92,
    capitalizacao_usd: 180000000000,
    volume_24h_usd: 5800000000,
    fonte: "scraping",
    coletado_em: "2026-09-16T16:30:00",
  },
];