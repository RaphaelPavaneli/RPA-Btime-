function Header() {
  return (
    <header className="border-b border-slate-800 bg-slate-900">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        <div>
          <h1 className="text-xl font-bold text-emerald-400">
            CryptoData
          </h1>

          <p className="text-sm text-slate-400">
            Monitoramento de criptomoedas
          </p>
        </div>

        <div className="flex items-center gap-2 text-sm text-slate-400">
          <span className="h-2 w-2 rounded-full bg-emerald-400" />
          Online
        </div>
      </div>
    </header>
  );
}

export default Header;