interface ActionButtonsProps {
  onAtualizar: () => void;
  isLoading: boolean;
}

function ActionButtons({ onAtualizar, isLoading }: ActionButtonsProps) {
  return (
    <div className="flex flex-wrap gap-3">
      <button
        type="button"
        onClick={onAtualizar}
        disabled={isLoading}
        className="
          rounded-lg
          border border-stone-300
          bg-white
          px-4 py-2
          text-sm font-medium
          text-stone-700
          shadow-sm
          transition
          hover:bg-stone-100
        "
      >
        Atualizar dados
      </button>

      <button
        type="button"
        className="
          rounded-lg
          bg-amber-500
          px-4 py-2
          text-sm font-semibold
          text-white
          shadow-sm
          transition
          hover:bg-amber-600
        "
      >
        Baixar CSV
      </button>
    </div>
  );
}

export default ActionButtons;