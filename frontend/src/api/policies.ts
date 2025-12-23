import { apiFetch } from "./client"

export function ingestPolicy(lenderId: string, file: File) {
  const form = new FormData()
  form.append("file", file)

  return fetch(`/api/v1/lenders/${lenderId}/policies/ingest`, {
    method: "POST",
    body: form,
  }).then(res => res.json())
}
