from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from sqlalchemy import func
import tempfile
import logging

from app.db.deps import get_db
from app.db.models import Policy, Rule
from app.schemas.policy import PolicyOut
from app.schemas.review import PolicyReview
from app.workflows.policy_ingestion import ingest_policy_document


router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/api/v1/lenders/{lender_id}/policies/ingest")
def ingest_policy(
    lender_id: str,
    file: UploadFile = File(...),
):
    logger.info(f"Received policy ingestion request for lender {lender_id}, file: {file.filename}")
    
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name
        logger.info(f"Saved uploaded file to temporary path: {tmp_path}")

    try:
        policy_id = ingest_policy_document(
            lender_id=lender_id,
            pdf_path=tmp_path,
        )
        logger.info(f"Policy ingestion completed successfully, policy ID: {policy_id}")
    except Exception as e:
        logger.error(f"Policy ingestion failed for lender {lender_id}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Policy ingestion failed: {str(e)}",
        )

    return {
        "policy_id": policy_id,
        "status": "draft_created",
    }

@router.post("/api/v1/policies/{policy_id}/activate")
def activate_policy(policy_id: str, db: Session = Depends(get_db)):
    logger.info(f"Activating policy {policy_id}")
    
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        logger.warning(f"Policy {policy_id} not found")
        raise HTTPException(status_code=404, detail="Policy not found")

    logger.info(f"Deactivating other active policies for lender {policy.lender_id}, program {policy.program}")
    # Deactivate others
    db.query(Policy).filter(
        Policy.lender_id == policy.lender_id,
        Policy.program == policy.program,
        Policy.active == True,
    ).update({"active": False})

    policy.active = True
    db.commit()
    logger.info(f"Policy {policy_id} activated successfully")

    return {"status": "activated"}

@router.get(
    "/api/v1/policies/{policy_id}",
    response_model=PolicyReview
)
def get_policy_for_review(
    policy_id: str,
    db: Session = Depends(get_db),
):
    logger.info(f"Retrieving policy {policy_id} for review")
    
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        logger.warning(f"Policy {policy_id} not found")
        raise HTTPException(status_code=404, detail="Policy not found")

    rules = db.query(Rule).filter(Rule.policy_id == policy.id).all()
    logger.info(f"Retrieved {len(rules)} rules for policy {policy_id}")

    return {
        "policy_id": policy.id,
        "lender_id": policy.lender_id,
        "version": policy.version,
        "active": policy.active,
        "rules": [
            {
                "rule_id": r.id,
                "rule_type": r.rule_type,
                "operator": r.operator,
                "value": r.value,
                "hard_rule": r.hard_rule,
            }
            for r in rules
        ],
    }


@router.post("/api/v1/policies/{policy_id}/approve")
def approve_policy(
    policy_id: str,
    db: Session = Depends(get_db),
):
    logger.info(f"Approving policy {policy_id}")
    
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        logger.warning(f"Policy {policy_id} not found")
        raise HTTPException(status_code=404, detail="Policy not found")

    rule_count = db.query(Rule).filter(Rule.policy_id == policy.id).count()
    logger.info(f"Policy {policy_id} has {rule_count} rules")
    if rule_count == 0:
        logger.warning(f"Cannot activate policy {policy_id} without rules")
        raise HTTPException(
            status_code=400,
            detail="Cannot activate policy without rules",
        )

    logger.info(f"Deactivating existing active policy for lender {policy.lender_id}, program {policy.program}")
    # Deactivate existing active policy
    db.query(Policy).filter(
        Policy.lender_id == policy.lender_id,
        Policy.program == policy.program,
        Policy.active == True,
    ).update({"active": False})

    policy.active = True
    db.commit()
    logger.info(f"Policy {policy_id} approved and activated successfully")

    return {"status": "policy_activated"}

