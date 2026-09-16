import type { Criptomoeda } from "../types/crypto";

const API_URL = "/api";

export async function buscarCriptomoedas(
  fonte: "api" | "scraping",
  limite = 10,
): Promise<Criptomoeda[]> {
  const response = await fetch(
    `${API_URL}/criptomoedas?fonte=${fonte}&limite=${limite}`,
  );

  if (!response.ok) {
    throw new Error("Não foi possível carregar os dados.");
  }

  return response.json();
}


export async function baixarCsv(
  fonte: "api" | "scraping",
  limite = 10,
): Promise<void> {
  const response = await fetch(
    `${API_URL}/criptomoedas/csv?fonte=${fonte}&limite=${limite}`,
  );

  if (!response.ok) {
    throw new Error("Não foi possível baixar o CSV.");
  }

  const blob = await response.blob();

  const url = window.URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = url;

  link.download =
    fonte === "api"
      ? "criptomoedas_api.csv"
      : "criptomoedas_scraping.csv";

  document.body.appendChild(link);

  link.click();

  link.remove();

  window.URL.revokeObjectURL(url);
}