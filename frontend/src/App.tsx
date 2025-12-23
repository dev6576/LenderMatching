import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Layout from "./components/Layout"
import Apply from "./pages/Borrower/Apply"
import Results from "./pages/Borrower/Results"
import History from "./pages/Borrower/History"
import Manage from "./pages/Lender/Manage"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
        {/*DEFAULT ROUTE*/}
        <Route path="/" element={<Navigate to="/borrower/apply" replace/>} />
        
          <Route path="/borrower/apply" element={<Apply />} />
          <Route path="/borrower/results" element={<Results />} />
          <Route path="/borrower/history" element={<History />} />
          <Route path="/lender/manage" element={<Manage />} />
        </Route>

      </Routes>
    </BrowserRouter>
  )
}
