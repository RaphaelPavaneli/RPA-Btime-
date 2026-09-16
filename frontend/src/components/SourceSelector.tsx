import { useState } from "react";

type Source = "api" | "scraping";

function SourceSelector() {
  const [source, setSource] = useState<Source>("api");

  return (
    <div className="flex w-fit rounded-lg bg-slate-900 p-1">
      <button
        type="button"
        onClick={() => setSource("api")}
        className={`rounded-md px-4 py-2 text-sm font-medium transition ${
          source === "api"
            ? "bg-emerald-500 text-slate-950"
            : "text-slate-400 hover:text-white"
        }`}
      >
        API
      </button>

      <button
        type="button"
        onClick={() => setSource("scraping")}
        className={`rounded-md px-4 py-2 text-sm font-medium transition ${
          source === "scraping"
            ? "bg-emerald-500 text-slate-950"
            : "text-slate-400 hover:text-white"
        }`}
      >
        Scraping
      </button>
    </div>
  );
}

export default SourceSelector;