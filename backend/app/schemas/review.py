from pydantic import BaseModel
from typing import Any, List
from uuid import UUID


class RuleReview(BaseModel):
    rule_id: UUID
    rule_type: str
    operator: str
    value: Any
    hard_rule: bool


class PolicyReview(BaseModel):
    policy_id: UUID
    lender_id: UUID
    version: int
    active: bool
    rules: List[RuleReview]
