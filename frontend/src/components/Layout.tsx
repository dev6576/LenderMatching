import { Outlet } from "react-router-dom"
import Nav from "./Nav"

export default function Layout() {
  return (
    <>
      <Nav />
      <div style={{ padding: 16 }}>
        <Outlet />
      </div>
    </>
  )
}
