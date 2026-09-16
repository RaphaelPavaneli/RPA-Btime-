export interface Criptomoeda {
  posicao: number;
  nome: string;
  simbolo: string;
  preco_usd: number;
  variacao_24h: number;
  capitalizacao_usd: number;
  volume_24h_usd: number;
  fonte: string;
  coletado_em: string;
}