from fastapi import APIRouter
from uuid import UUID, uuid4

router = APIRouter()


@router.post("")
def create_application(payload: dict):
    """
    Create a loan application.
    """
    application_id = uuid4()
    return {
        "application_id": application_id,
        "status": "CREATED"
    }


@router.get("/{application_id}")
def get_application(application_id: UUID):
    """
    Fetch a loan application.
    """
    return {
        "application_id": application_id,
        "status": "CREATED",
        "data": {}
    }
