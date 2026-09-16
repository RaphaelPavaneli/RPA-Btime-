import { useState } from "react";

type Source = "api" | "scraping";

function SourceSelector() {
  const [source, setSource] = useState<Source>("api");

  return (
    <div className="flex w-fit rounded-lg border border-stone-200 bg-white p-1 shadow-sm">
      <button
        type="button"
        onClick={() => setSource("api")}
        className={`rounded-md px-4 py-2 text-sm font-medium transition ${
          source === "api"
            ? "bg-amber-500 text-white shadow-sm"
            : "text-stone-500 hover:bg-amber-50 hover:text-stone-800"
        }`}
      >
        API
      </button>

      <button
        type="button"
        onClick={() => setSource("scraping")}
        className={`rounded-md px-4 py-2 text-sm font-medium transition ${
          source === "scraping"
            ? "bg-amber-500 text-white shadow-sm"
            : "text-stone-500 hover:bg-amber-50 hover:text-stone-800"
        }`}
      >
        Scraping
      </button>
    </div>
  );
}

export default SourceSelector;