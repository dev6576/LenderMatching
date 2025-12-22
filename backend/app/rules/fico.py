from app.rules.base import BaseRule, RuleResult


class FicoRule(BaseRule):
    rule_type = "min_fico"
    hard_rule = True

    def evaluate(self, application: dict) -> RuleResult:
        applicant_fico = application["guarantor"]["fico_score"]
        required_fico = int(self.value)

        passed = applicant_fico >= required_fico

        explanation = (
            f"Applicant FICO {applicant_fico} meets minimum required {required_fico}"
            if passed
            else f"Applicant FICO {applicant_fico} is below minimum required {required_fico}"
        )

        return RuleResult(
            rule_type=self.rule_type,
            passed=passed,
            explanation=explanation
        )
