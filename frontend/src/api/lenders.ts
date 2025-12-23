import { apiFetch } from "./client"
import type { Lender } from "../types/lender"

export function listLenders(): Promise<Lender[]> {
  return apiFetch("/api/v1/lenders")
}

export function createLender(name: string) {
  return apiFetch("/api/v1/lenders", {
    method: "POST",
    body: JSON.stringify({ name }),
  })
}