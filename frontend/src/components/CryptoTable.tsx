import type { Criptomoeda } from "../types/crypto";

interface CryptoTableProps {
  criptomoedas: Criptomoeda[];
}

function CryptoTable({ criptomoedas }: CryptoTableProps) {
  return (
    <div className="mt-8 overflow-x-auto rounded-xl border border-slate-800 bg-slate-900">
      <table className="min-w-full text-left text-sm">
        <thead className="border-b border-slate-800 bg-slate-900">
          <tr className="text-slate-400">
            <th className="px-4 py-3">#</th>
            <th className="px-4 py-3">Criptomoeda</th>
            <th className="px-4 py-3">Preço</th>
            <th className="px-4 py-3">Variação 24h</th>
            <th className="px-4 py-3">Capitalização</th>
            <th className="px-4 py-3">Volume 24h</th>
            <th className="px-4 py-3">Fonte</th>
            <th className="px-4 py-3">Coletado em</th>
          </tr>
        </thead>

        <tbody>
          {criptomoedas.map((crypto) => (
            <tr
              key={`${crypto.simbolo}-${crypto.posicao}`}
              className="border-b border-slate-800 last:border-b-0 hover:bg-slate-800/50"
            >
              <td className="px-4 py-4 text-slate-400">
                {crypto.posicao}
              </td>

              <td className="px-4 py-4">
                <div>
                  <p className="font-medium text-white">
                    {crypto.nome}
                  </p>

                  <p className="text-xs uppercase text-slate-500">
                    {crypto.simbolo}
                  </p>
                </div>
              </td>

              <td className="px-4 py-4 text-slate-200">
                {formatarMoeda(crypto.preco_usd)}
              </td>

              <td
                className={`px-4 py-4 font-medium ${
                  crypto.variacao_24h >= 0
                    ? "text-emerald-400"
                    : "text-red-400"
                }`}
              >
                {formatarVariacao(crypto.variacao_24h)}
              </td>

              <td className="px-4 py-4 text-slate-200">
                {formatarNumeroCompacto(crypto.capitalizacao_usd)}
              </td>

              <td className="px-4 py-4 text-slate-200">
                {formatarNumeroCompacto(crypto.volume_24h_usd)}
              </td>

              <td className="px-4 py-4">
                <span className="rounded-full bg-slate-800 px-2 py-1 text-xs uppercase text-slate-300">
                  {crypto.fonte}
                </span>
              </td>

              <td className="px-4 py-4 text-slate-400">
                {formatarData(crypto.coletado_em)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function formatarMoeda(valor: number) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 2,
  }).format(valor);
}

function formatarNumeroCompacto(valor: number) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    notation: "compact",
    maximumFractionDigits: 2,
  }).format(valor);
}

function formatarVariacao(valor: number) {
  const sinal = valor > 0 ? "+" : "";

  return `${sinal}${valor.toFixed(2)}%`;
}

function formatarData(data: string) {
  return new Intl.DateTimeFormat("pt-BR", {
    dateStyle: "short",
    timeStyle: "short",
  }).format(new Date(data));
}

export default CryptoTable;