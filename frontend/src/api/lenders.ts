import { apiFetch } from "./client";
import type { Lender } from "../types/lender";

export function listLenders(): Promise<Lender[]> {
  return apiFetch("/api/lenders");
}

export function createLender(name: string): Promise<Lender> {
  return apiFetch("/api/lenders", {
    method: "POST",
    body: JSON.stringify({ name }),
  });
}
