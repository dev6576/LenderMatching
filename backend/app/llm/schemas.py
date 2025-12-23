from pydantic import BaseModel, Field
from typing import List, Optional


class RuleCandidate(BaseModel):
    rule_type: str
    operator: str
    value: str | int | float
    hard_rule: bool
    notes: Optional[str] = None


class LLMRuleExtraction(BaseModel):
    rules: List[RuleCandidate]
    assumptions: List[str] = []
    unmapped_sections: List[str] = []
