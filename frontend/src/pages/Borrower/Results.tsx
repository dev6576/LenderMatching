import { useLocation } from "react-router-dom"

export default function Results() {
  const { state } = useLocation()

  return (
    <>
      <h2>Results</h2>

      <h3>Eligible Lenders</h3>
      {state.eligible_lenders.map((l: any) => (
        <div key={l.lendider_id}>
          <strong>{l.id}</strong>
          <p>{l.llm_explanation}</p>
        </div>
      ))}

      <h3>Rejected Lenders</h3>
      {state.rejected_lenders.map((l: any) => (
        <div key={l.id}>
          <strong>{l.id}</strong>
          <p>{l.llm_explanation}</p>
        </div>
      ))}
    </>
  )
}
