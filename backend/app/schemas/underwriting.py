from pydantic import BaseModel
from typing import Any

class UnderwritingRequest(BaseModel):
    application: dict


class RuleEvaluation(BaseModel):
    rule_type: str
    passed: bool
    explanation: str


class UnderwritingResult(BaseModel):
    lender_id: str
    eligible: bool
    fit_score: int | None
    evaluations: list[RuleEvaluation]
