import { useEffect, useState } from "react"
import { createLender, listLenders } from "../../api/lenders"
import { ingestPolicy } from "../../api/policies"

export default function Manage() {
  const [lenders, setLenders] = useState<any[]>([])
  const [selectedLenderId, setSelectedLenderId] = useState("")
  const [file, setFile] = useState<File | null>(null)
  const [newLenderName, setNewLenderName] = useState("")

  useEffect(() => {
    listLenders().then(setLenders)
  }, [])

  const addLender = async () => {
    if (!newLenderName.trim()) return
    await createLender(newLenderName)
    setNewLenderName("")
    const updated = await listLenders()
    setLenders(updated)
  }

  const upload = async () => {
    if (!file || !selectedLenderId) return
    await ingestPolicy(selectedLenderId, file)
    alert("Policy uploaded")
  }

  return (
    <>
      <h2>Lender Management</h2>

      <h3>Add New Lender</h3>
      <input
        placeholder="Lender name"
        value={newLenderName}
        onChange={e => setNewLenderName(e.target.value)}
      />
      <button onClick={addLender}>Add</button>

      <hr />

      <h3>Upload Policy Document</h3>
      <select
        value={selectedLenderId}
        onChange={e => setSelectedLenderId(e.target.value)}
      >
        <option value="" disabled>
          Select Lender
        </option>
        {lenders.map(l => (
          <option key={l.id} value={l.id}>
            {l.name}
          </option>
        ))}
      </select>

      <br />
      <input
        type="file"
        accept="application/pdf"
        onChange={e => setFile(e.target.files?.[0] || null)}
      />
      <br />
      <button onClick={upload} disabled={!file || !selectedLenderId}>
        Upload Policy PDF
      </button>
    </>
  )
}
