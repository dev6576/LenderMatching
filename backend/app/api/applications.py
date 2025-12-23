from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.db.models import LoanApplicationRecord

router = APIRouter()


@router.get("/")
def list_loan_applications(db: Session = Depends(get_db)):
    apps = (
        db.query(LoanApplicationRecord)
        .order_by(LoanApplicationRecord.submitted_at.desc())
        .limit(20)
        .all()
    )

    return [
        {
            "id": str(a.id),
            "submitted_at": a.submitted_at,
            "application_payload": a.application_payload,
            "underwriting_result": a.underwriting_result,
        }
        for a in apps
    ]
