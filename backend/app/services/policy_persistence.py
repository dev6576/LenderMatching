from uuid import uuid4
import logging
from typing import Dict, Any

from app.db.database import SessionLocal
from app.db.models import Policy, Rule, PolicyDocument

logger = logging.getLogger(__name__)


def persist_policy_draft(
    lender_id: str,
    raw_text: str,
    llm_result: Dict[str, Any],
) -> str:
    """
    Persists a draft policy and its rules extracted from an LLM.

    Expected llm_result shape:
    {
        "rules": [
            {
                "rule_type": str,
                "operator": str,
                "value": int | float | str,
                "hard_rule": bool
            }
        ],
        "assumptions": [...],
        "unmapped_sections": [...]
    }
    """
    logger.info("Persisting policy draft for lender %s", lender_id)
    db = SessionLocal()

    try:
        # 1. Store original document
        logger.info("Storing policy document")
        document = PolicyDocument(
            lender_id=lender_id,
            filename="uploaded.pdf",
            content_type="application/pdf",
            raw_text=raw_text,
            llm_assumptions=llm_result.get("assumptions"),
            llm_unmapped_sections=llm_result.get("unmapped_sections"),
        )
        db.add(document)
        db.flush()
        logger.debug("PolicyDocument stored with ID %s", document.id)

        # 2. Determine next policy version
        latest_policy = (
            db.query(Policy)
            .filter(Policy.lender_id == lender_id)
            .order_by(Policy.version.desc())
            .first()
        )

        next_version = (latest_policy.version + 1) if latest_policy else 1
        logger.info("Next policy version resolved as %d", next_version)

        # 3. Create draft policy
        policy = Policy(
            id=uuid4(),
            lender_id=lender_id,
            program="DEFAULT",
            version=next_version,
            active=False,  # draft
        )
        db.add(policy)
        db.flush()
        logger.info("Created draft policy with ID %s", policy.id)

        # 4. Create rules
        rules = llm_result.get("rules", [])
        logger.info("Creating %d rules for policy %s", len(rules), policy.id)

        for rule in rules:
            db.add(
                Rule(
                    id=uuid4(),
                    policy_id=policy.id,
                    rule_type=rule["rule_type"],
                    operator=rule["operator"],
                    value={"value": rule["value"]},
                    hard_rule=rule["hard_rule"],
                )
            )

        # 5. Link document to policy
        document.policy_id = policy.id

        db.commit()
        logger.info("Successfully persisted policy draft %s", policy.id)
        return str(policy.id)

    except Exception as e:
        db.rollback()
        logger.exception(
            "Failed to persist policy draft for lender %s", lender_id
        )
        raise

    finally:
        db.close()
