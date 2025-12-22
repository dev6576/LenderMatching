from fastapi import APIRouter
from uuid import UUID, uuid4

router = APIRouter()


@router.post("/run")
def start_underwriting(payload: dict):
    """
    Trigger Hatchet underwriting workflow.
    """
    run_id = uuid4()
    return {
        "run_id": run_id,
        "status": "STARTED"
    }


@router.get("/{run_id}/status")
def get_underwriting_status(run_id: UUID):
    """
    Poll underwriting workflow status.
    """
    return {
        "run_id": run_id,
        "status": "IN_PROGRESS",
        "completed_lenders": 0,
        "total_lenders": 0
    }
