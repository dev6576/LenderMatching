import { useState } from "react";

type Props = {
  onCreate: (name: string) => void;
};

export default function LenderForm({ onCreate }: Props) {
  const [name, setName] = useState("");

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        if (!name.trim()) return;
        onCreate(name);
        setName("");
      }}
    >
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Lender name"
      />
      <button type="submit">Add Lender</button>
    </form>
  );
}
