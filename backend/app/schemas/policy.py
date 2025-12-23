from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class RuleSchema(BaseModel):
    rule_type: str
    operator: str
    value: str
    hard_rule: bool = True
    weight: Optional[int] = None


class PolicyCreateRequest(BaseModel):
    lender_id: UUID
    program: str
    rules: List[RuleSchema]


class PolicyResponse(BaseModel):
    policy_id: UUID
    lender_id: UUID
    program: str
    version: int


class PolicyOut(BaseModel):
    policy_id: UUID
    lender_id: UUID
    program: str
    version: int
    active: bool

    class Config:
        orm_mode = True
