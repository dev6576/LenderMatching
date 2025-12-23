import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { evaluateUnderwriting } from "../../api/underwriting"

export default function Apply() {
  const [form, setForm] = useState({
    credit_score: 700,
    years_in_business: 3,
    loan_amount: 50000,
  })

  const navigate = useNavigate()

  const submit = async () => {
    const result = await evaluateUnderwriting(form)
    navigate("/borrower/results", { state: result })
  }

  return (
    <>
      <h2>Apply for Loan</h2>
      <input
        type="number"
        placeholder="Credit Score"
        value={form.credit_score}
        onChange={e => setForm({ ...form, credit_score: +e.target.value })}
      />
      <br />
      <input
        type="number"
        placeholder="Years in Business"
        value={form.years_in_business}
        onChange={e => setForm({ ...form, years_in_business: +e.target.value })}
      />
      <br />
      <input
        type="number"
        placeholder="Loan Amount"
        value={form.loan_amount}
        onChange={e => setForm({ ...form, loan_amount: +e.target.value })}
      />
      <br />
      <button onClick={submit}>Submit</button>
    </>
  )
}
