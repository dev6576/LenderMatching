from fastapi import APIRouter
from uuid import UUID

router = APIRouter()


@router.get("/{run_id}")
def get_results(run_id: UUID):
    """
    Fetch underwriting match results.
    """
    return {
        "application_id": "uuid",
        "results": []
    }
