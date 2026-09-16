import type { Criptomoeda } from "../types/crypto";

interface CryptoTableProps {
  criptomoedas: Criptomoeda[];
  isLoading?: boolean;
  error?: string | null;
}

function CryptoTable({criptomoedas, isLoading = false, error = null,}: CryptoTableProps) {
    if (isLoading) {
    return (
      <div className="mt-8 rounded-xl border border-stone-200 bg-white px-6 py-12 text-center shadow-sm">
      <div className="flex flex-col items-center gap-3">
        <div className="h-6 w-6 animate-spin rounded-full border-2 border-stone-300 border-t-amber-500" />

        <p className="text-sm font-medium text-stone-600">
          Carregando dados...
        </p>
      </div>
    </div>
    );
    }

    if (error) {
    return (
        <div className="mt-8 rounded-xl border border-stone-200 bg-white px-6 py-12 text-center shadow-sm">
        <h3 className="text-lg font-semibold text-stone-800">
            Não foi possível carregar os dados
        </h3>

        <p className="mt-2 text-sm text-red-500">
            {error}
        </p>
        </div>
        );
    }
    
    if (criptomoedas.length === 0) {
    return (
        <div className="mt-8 rounded-xl border border-dashed border-slate-700 bg-slate-900/50 px-6 py-12 text-center">
            <h3 className="text-lg font-semibold text-slate-200">
            Nenhuma criptomoeda encontrada
            </h3>

            <p className="mt-2 text-sm text-slate-400">
            Atualize os dados ou selecione outra fonte de coleta.
            </p>
        </div>
        );
    }

    return (
        <div className="mt-8 overflow-x-auto rounded-xl border border-stone-200 bg-white shadow-sm">
        <table className="min-w-full text-left text-sm">
            <thead className="border-b border-stone-200 bg-amber-50/70">
            <tr key={`${crypto.simbolo}-${crypto.posicao}`}
                className="border-b border-stone-100 last:border-b-0 hover:bg-amber-50/40"
            >
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
                    className="
                    border-b border-stone-200
                    last:border-b-0
                    transition-colors
                    hover:bg-amber-50/60
                    "
                >
                    <td className="px-4 py-4 text-stone-500">
                    {crypto.posicao}
                    </td>

                    <td className="px-4 py-4">
                    <div>
                        <p className="font-semibold text-stone-900">
                        {crypto.nome}
                        </p>

                        <p className="text-xs font-medium uppercase text-stone-500">
                        {crypto.simbolo}
                        </p>
                    </div>
                    </td>

                    <td className="px-4 py-4 font-medium text-stone-800">
                    {formatarMoeda(crypto.preco_usd)}
                    </td>

                    <td
                    className={`px-4 py-4 font-semibold ${
                        crypto.variacao_24h >= 0
                        ? "text-emerald-600"
                        : "text-red-500"
                    }`}
                    >
                    {formatarVariacao(crypto.variacao_24h)}
                    </td>

                    <td className="px-4 py-4 text-stone-700">
                    {formatarNumeroCompacto(crypto.capitalizacao_usd)}
                    </td>

                    <td className="px-4 py-4 text-stone-700">
                    {formatarNumeroCompacto(crypto.volume_24h_usd)}
                    </td>

                    <td className="px-4 py-4">
                    <span
                        className="
                            rounded-full
                            bg-stone-200
                            px-2.5 py-1
                            text-xs
                            font-medium
                            uppercase
                            text-stone-800
                        "
                    >
                        {crypto.fonte}
                    </span>
                    </td>

                    <td className="px-4 py-4 text-stone-500">
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