import { apiFetch } from "./client"
import type { LoanApplication, UnderwritingResponse } from "../types/underwriting"

export function evaluateUnderwriting(
  payload: LoanApplication
): Promise<UnderwritingResponse> {
  return apiFetch("/api/v1/underwriting/evaluate", {
    method: "POST",
    body: JSON.stringify(payload),
  })
}
