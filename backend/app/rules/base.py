from dataclasses import dataclass
from typing import Optional


@dataclass
class RuleResult:
    rule_type: str
    passed: bool
    explanation: str
    score_impact: Optional[int] = None


from abc import ABC, abstractmethod
from typing import Any
from app.rules.base import RuleResult


class BaseRule(ABC):
    rule_type: str
    hard_rule: bool = True

    def __init__(self, operator: str, value: Any, weight: int = 0):
        self.operator = operator
        self.value = value
        self.weight = weight

    @abstractmethod
    def evaluate(self, application: dict) -> RuleResult:
        """
        Evaluate rule against application snapshot.
        Must return RuleResult with explanation.
        """
        pass

