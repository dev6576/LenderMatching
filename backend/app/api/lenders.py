from fastapi import APIRouter
from uuid import UUID

router = APIRouter()


@router.get("")
def list_lenders():
    """
    List all lenders.
    """
    return []


@router.get("/{lender_id}")
def get_lender(lender_id: UUID):
    """
    Get lender details.
    """
    return {
        "lender_id": lender_id,
        "name": "Sample Lender"
    }
