from app.rules.base import BaseRule, RuleResult


class TimeInBusinessRule(BaseRule):
    rule_type = "min_time_in_business"
    hard_rule = True

    def evaluate(self, application: dict) -> RuleResult:
        years = application["borrower"]["years_in_business"]
        required = int(self.value)

        passed = years >= required

        explanation = (
            f"Business age {years} years meets minimum required {required} years"
            if passed
            else f"Business age {years} years is below minimum required {required} years"
        )

        return RuleResult(
            rule_type=self.rule_type,
            passed=passed,
            explanation=explanation
        )
