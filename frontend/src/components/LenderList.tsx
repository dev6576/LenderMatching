import type { Lender } from "../types/lender";

type Props = {
  lenders: Lender[];
};

export default function LenderList({ lenders }: Props) {
  return (
    <ul>
      {lenders.map((l) => (
        <li key={l.id}>{l.name}</li>
      ))}
    </ul>
  );
}
