import { apiFetch } from "./client"
import type { ApplicationRecord } from "../types/application"

export function listApplications(): Promise<ApplicationRecord[]> {
  return apiFetch("/api/v1/applications")
}
