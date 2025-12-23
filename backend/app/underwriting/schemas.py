from pydantic import BaseModel
from typing import List, Dict, Any


class LoanApplication(BaseModel):
    credit_score: int
    years_in_business: int
    loan_amount: int


class RuleExplanation(BaseModel):
    rule_type: str
    operator: str
    expected: Any
    actual: Any
    result: str
    hard_rule: bool


class UnderwritingResult(BaseModel):
    eligible: bool
    hard_failures: List[RuleExplanation]
    soft_warnings: List[RuleExplanation]
    explanation: List[RuleExplanation]
