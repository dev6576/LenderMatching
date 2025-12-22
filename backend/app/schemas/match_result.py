from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class RuleEvaluationResult(BaseModel):
    rule_type: str
    status: str  # PASSED / FAILED
    explanation: str


class LenderMatchResult(BaseModel):
    lender_id: UUID
    lender_name: str
    eligible: bool
    fit_score: Optional[int]
    program: Optional[str]
    reasons: List[RuleEvaluationResult]


class MatchResultsResponse(BaseModel):
    application_id: UUID
    results: List[LenderMatchResult]
