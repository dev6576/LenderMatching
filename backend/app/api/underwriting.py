from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.db.models import Policy, Rule, LoanApplicationRecord
from app.underwriting.schemas import LoanApplication
from app.underwriting.evaluator import evaluate_policy
from app.underwriting.explainer import generate_underwriting_explanation

router = APIRouter()


@router.post("/evaluate")
def evaluate_underwriting_all_lenders(
    application: LoanApplication,
    db: Session = Depends(get_db),
):
    print("[API] Starting underwriting evaluation for ALL lenders")
    print(f"[API] Application: {application.dict()}")

    policies = (
        db.query(Policy)
        .filter(Policy.active == True)
        .all()
    )

    print(f"[API] Found {len(policies)} active policies")

    eligible_lenders = []
    rejected_lenders = []

    for policy in policies:
        print("-" * 60)
        print(f"[API] Evaluating lender {policy.lender_id} | policy {policy.id}")

        rules = (
            db.query(Rule)
            .filter(Rule.policy_id == policy.id)
            .all()
        )

        print(f"[API] Loaded {len(rules)} rules")

        eligible, hard_failures, soft_warnings, explanation = evaluate_policy(
            rules,
            application.dict()
        )

        print("[API] Generating LLM explanation")
        llm_explanation = generate_underwriting_explanation(
            lender_id=str(policy.lender_id),
            eligible=eligible,
            hard_failures=hard_failures,
            soft_warnings=soft_warnings,
        )

        result = {
            "lender_id": str(policy.lender_id),
            "policy_id": str(policy.id),
            "eligible": eligible,
            "hard_failures": hard_failures,
            "soft_warnings": soft_warnings,
            "explanation": explanation,
            "llm_explanation": llm_explanation,
        }

        if eligible:
            print(f"[API] Lender {policy.lender_id} → ELIGIBLE")
            eligible_lenders.append(result)
        else:
            print(f"[API] Lender {policy.lender_id} → REJECTED")
            rejected_lenders.append(result)

    print("[API] Underwriting evaluation completed")

    print("[API] Persisting loan application")

    record = LoanApplicationRecord(
        id=uuid4(),
        application_payload=application.dict(),
        underwriting_result={
            "eligible_lenders": eligible_lenders,
            "rejected_lenders": rejected_lenders,
        },
    )

    db.add(record)
    db.commit()

    print(f"[API] Loan application stored with ID {record.id}")
    return {
        "eligible_lenders": eligible_lenders,
        "rejected_lenders": rejected_lenders,
    }
