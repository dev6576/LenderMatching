from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.db.models import Lender, Policy


def get_active_lender_ids(db: Session) -> List[UUID]:
    """
    Returns lender IDs that:
    - Are active
    - Have at least one active policy
    """

    rows = (
        db.query(Lender.id)
        .join(Policy, Policy.lender_id == Lender.id)
        .filter(
            Lender.active == True,
            Policy.active == True,
        )
        .distinct()
        .all()
    )

    return [row.id for row in rows]
