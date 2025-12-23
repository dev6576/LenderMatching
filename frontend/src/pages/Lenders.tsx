import { useEffect, useState } from "react";
import { listLenders, createLender } from "../api/lenders";
import type { Lender } from "../types/lender";
import LenderForm from "../components/LenderForm";
import LenderList from "../components/LenderList";

export default function LendersPage() {
  const [lenders, setLenders] = useState<Lender[]>([]);

  useEffect(() => {
    listLenders().then(setLenders);
  }, []);

  async function handleCreate(name: string) {
    const newLender = await createLender(name);
    setLenders((prev) => [...prev, newLender]);
  }

  return (
    <div>
      <h1>Lenders</h1>
      <LenderForm onCreate={handleCreate} />
      <LenderList lenders={lenders} />
    </div>
  );
}
