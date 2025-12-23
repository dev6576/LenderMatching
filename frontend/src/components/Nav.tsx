import { Link } from "react-router-dom"

export default function Nav() {
  return (
    <nav style={{ padding: 12, borderBottom: "1px solid #ddd" }}>
      <Link to="/borrower/apply">Apply</Link>{" | "}
      <Link to="/borrower/history">History</Link>{" | "}
      <Link to="/lender/manage">Lender</Link>
    </nav>
  )
}
