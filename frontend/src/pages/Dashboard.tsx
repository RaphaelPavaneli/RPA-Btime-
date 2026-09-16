import { useState } from "react";

import Header from "../components/Header";
import SourceSelector from "../components/SourceSelector";
import ActionButtons from "../components/ActionButtons";
import CryptoTable from "../components/CryptoTable";

import { buscarCriptomoedas, baixarCsv, } from "../services/cryptoService";

import type { Criptomoeda } from "../types/crypto";

type Fonte = "api" | "scraping";

function Dashboard() {
  const [fonte, setFonte] = useState<Fonte>("api");
  const [criptomoedas, setCriptomoedas] = useState<Criptomoeda[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleBaixarCsv() {
    try {
      setError(null);

      await baixarCsv(fonte);
    } catch (erro) {
      setError(
        erro instanceof Error
          ? erro.message
          : "Erro inesperado ao baixar o CSV.",
      );
    }
  }

  async function carregarDados() {
    try {
      setIsLoading(true);
      setError(null);

      const dados = await buscarCriptomoedas(fonte);

      setCriptomoedas(dados);
    } catch (erro) {
      setCriptomoedas([]);

      setError(
        erro instanceof Error
          ? erro.message
          : "Erro inesperado ao carregar os dados.",
      );
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-stone-50 text-stone-800">
      <Header />

      <main className="mx-auto max-w-7xl px-6 py-10">
        <h2 className="text-3xl font-bold text-stone-800">
          Mercado de Criptomoedas
        </h2>

        <p className="mt-2 text-stone-500">
          Consulte dados coletados via API ou Web Scraping.
        </p>

        <div className="mt-8 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <SourceSelector
            source={fonte}
            onChange={setFonte}
          />
          <ActionButtons
            onAtualizar={carregarDados}
            onBaixarCsv={handleBaixarCsv}
            isLoading={isLoading}
          />
        </div>

        <CryptoTable
          criptomoedas={criptomoedas}
          isLoading={isLoading}
          error={error}
        />
      </main>
    </div>
  );
}

export default Dashboard;