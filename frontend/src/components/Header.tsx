function Header() {
  return (
    <header className="border-b border-stone-200 bg-amber-50/60">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        <div>
          <h1 className="text-xl font-bold text-amber-700">
            CryptoData
          </h1>

          <p className="text-sm text-stone-500">
            Monitoramento de criptomoedas
          </p>
        </div>

        <div className="flex items-center gap-2 text-sm text-stone-500">
          <span className="h-2 w-2 rounded-full bg-emerald-500" />
          Online
        </div>
      </div>
    </header>
  );
}

export default Header;