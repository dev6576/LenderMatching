import { useEffect, useState } from "react"
import { listApplications } from "../../api/application"

export default function History() {
  const [apps, setApps] = useState<any[]>([])

  useEffect(() => {
    listApplications().then(setApps)
  }, [])

  return (
    <>
      <h2>Application History</h2>
      {apps.map(a => (
        <div key={a.id}>
          <strong>{a.submitted_at}</strong>
          <pre>{JSON.stringify(a.application_payload, null, 2)}</pre>
        </div>
      ))}
    </>
  )
}
