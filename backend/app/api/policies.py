from fastapi import APIRouter, UploadFile, File
from uuid import UUID, uuid4

router = APIRouter()


@router.get("/{lender_id}/policies")
def get_policies(lender_id: UUID):
    """
    Get policies for a lender.
    """
    return []


@router.post("")
def create_policy(payload: dict):
    """
    Create a lender policy.
    """
    return {
        "policy_id": uuid4(),
        "status": "CREATED"
    }


@router.put("/{policy_id}")
def update_policy(policy_id: UUID, payload: dict):
    """
    Update a lender policy.
    """
    return {
        "policy_id": policy_id,
        "status": "UPDATED"
    }


@router.post("/ingest/pdf")
def ingest_pdf(file: UploadFile = File(...)):
    """
    Upload and extract lender PDF.
    """
    ingestion_id = uuid4()
    return {
        "ingestion_id": ingestion_id,
        "status": "EXTRACTED",
        "rule_candidates": 0
    }


@router.post("/ingest/{ingestion_id}/confirm")
def confirm_ingestion(ingestion_id: UUID):
    """
    Confirm extracted rules and persist.
    """
    return {
        "ingestion_id": ingestion_id,
        "status": "CONFIRMED"
    }
