from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import uuid4

from app.db.deps import get_db
from app.db.models import Lender
from app.schemas.lender import LenderOut

router = APIRouter()


@router.get("", response_model=list[LenderOut])
def list_lenders(db: Session = Depends(get_db)):
    lenders = db.query(Lender).filter(Lender.active == True).all()
    return [
        {"lender_id": l.id, "name": l.name}
        for l in lenders
    ]


@router.post("", response_model=LenderOut)
def create_lender(payload: dict, db: Session = Depends(get_db)):
    lender = Lender(
        id=uuid4(),
        name=payload["name"]
    )
    db.add(lender)
    db.commit()
    db.refresh(lender)

    return {
        "lender_id": lender.id,
        "name": lender.name
    }
