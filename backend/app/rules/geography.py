from app.rules.base import BaseRule, RuleResult


class GeographyRule(BaseRule):
    rule_type = "allowed_states"
    hard_rule = True

    def evaluate(self, application: dict) -> RuleResult:
        state = application["borrower"]["state"]
        allowed_states = set(self.value)

        passed = state in allowed_states

        explanation = (
            f"State {state} is allowed"
            if passed
            else f"State {state} is not in allowed states"
        )

        return RuleResult(
            rule_type=self.rule_type,
            passed=passed,
            explanation=explanation
        )
