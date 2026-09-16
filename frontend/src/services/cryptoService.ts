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