from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4

from app.db.deps import get_db
from app.db.models import Rule, Policy
from app.schemas.rule import RuleCreate, RuleOut, RuleUpdate

router = APIRouter()


@router.post(
    "/api/v1/policies/{policy_id}/rules",
    response_model=RuleOut
)
def create_rule(
    policy_id: str,
    payload: RuleCreate,
    db: Session = Depends(get_db),
):
    policy = db.query(Policy).filter(Policy.id == policy_id).first()
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")

    rule = Rule(
        id=uuid4(),
        policy_id=policy_id,
        **payload.dict()
    )

    db.add(rule)
    db.commit()
    db.refresh(rule)

    return {
        "rule_id": rule.id,
        **payload.dict()
    }


@router.get(
    "/api/v1/policies/{policy_id}/rules",
    response_model=list[RuleOut]
)
def list_rules(policy_id: str, db: Session = Depends(get_db)):
    rules = db.query(Rule).filter(Rule.policy_id == policy_id).all()
    return [
        {
            "rule_id": r.id,
            "rule_type": r.rule_type,
            "operator": r.operator,
            "value": r.value,
            "hard_rule": r.hard_rule,
            "weight": r.weight,
        }
        for r in rules
    ]


@router.delete("/api/v1/rules/{rule_id}")
def delete_rule(rule_id: str, db: Session = Depends(get_db)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    db.delete(rule)
    db.commit()

    return {"status": "deleted"}
