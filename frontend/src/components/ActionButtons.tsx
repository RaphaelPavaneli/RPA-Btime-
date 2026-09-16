function ActionButtons() {
  return (
    <div className="flex flex-wrap gap-3">
      <button
        type="button"
        className="
          rounded-lg
          border border-slate-700
          bg-slate-900
          px-4 py-2
          text-sm font-medium
          text-slate-200
          transition
          hover:border-slate-600
          hover:bg-slate-800
        "
      >
        Atualizar dados
      </button>

      <button
        type="button"
        className="
          rounded-lg
          bg-emerald-500
          px-4 py-2
          text-sm font-semibold
          text-slate-950
          transition
          hover:bg-emerald-400
        "
      >
        Baixar CSV
      </button>
    </div>
  );
}

export default ActionButtons;