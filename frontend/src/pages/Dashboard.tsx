import Header from "../components/Header";
import SourceSelector from "../components/SourceSelector";
import ActionButtons from "../components/ActionButtons";
import CryptoTable from "../components/CryptoTable";
import { criptomoedasMock } from "../mocks/cryptocurrencies";


function Dashboard() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <Header />

      <main className="mx-auto max-w-7xl px-6 py-10">
        <h2 className="text-3xl font-bold">
          Mercado de Criptomoedas
        </h2>

        <p className="mt-2 text-slate-400">
          Consulte dados coletados via API ou Web Scraping.
        </p>

        <div className="mt-8 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <SourceSelector />
          <ActionButtons />

        </div>
        
          <CryptoTable criptomoedas={criptomoedasMock} />

      </main>
    </div>
  );
}

export default Dashboard;