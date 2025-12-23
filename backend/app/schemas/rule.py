from pydantic import BaseModel
from uuid import UUID
from typing import Any

class RuleCreate(BaseModel):
    rule_type: str
    operator: str
    value: Any
    hard_rule: bool
    weight: int | None = None


class RuleOut(RuleCreate):
    rule_id: UUID

    class Config:
        orm_mode = True

class RuleUpdate(BaseModel):
    rule_type: str
    operator: str
    value: Any
    hard_rule: bool