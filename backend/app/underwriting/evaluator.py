from typing import Dict, Any, List
from app.db.models import Rule
from app.underwriting.schemas import RuleExplanation


def evaluate_rule(rule: Rule, application: Dict[str, Any]) -> RuleExplanation:
    """
    Evaluate a single rule against the application.
    """

    rule_value = rule.value["value"]
    applicant_value = application.get(rule.rule_type)

    print(f"[EVAL] Rule {rule.rule_type} {rule.operator} {rule_value}")
    print(f"[EVAL] Applicant value: {applicant_value}")

    passed = False

    if rule.operator == ">=":
        passed = applicant_value >= rule_value
    elif rule.operator == "<=":
        passed = applicant_value <= rule_value
    elif rule.operator == "==":
        passed = applicant_value == rule_value
    elif rule.operator == "!=":
        passed = applicant_value != rule_value
    else:
        raise ValueError(f"Unsupported operator: {rule.operator}")

    result = "PASS" if passed else "FAIL"

    print(f"[EVAL] Result: {result} (hard={rule.hard_rule})")

    return RuleExplanation(
        rule_type=rule.rule_type,
        operator=rule.operator,
        expected=rule_value,
        actual=applicant_value,
        result=result,
        hard_rule=rule.hard_rule,
    )


def evaluate_policy(rules: List[Rule], application: Dict[str, Any]):
    """
    Evaluate all rules in a policy.
    """

    explanation = []
    hard_failures = []
    soft_warnings = []

    print(f"[POLICY] Evaluating {len(rules)} rules")

    for rule in rules:
        exp = evaluate_rule(rule, application)
        explanation.append(exp)

        if exp.result == "FAIL":
            if exp.hard_rule:
                hard_failures.append(exp)
            else:
                soft_warnings.append(exp)

    eligible = len(hard_failures) == 0

    print(f"[POLICY] Eligible: {eligible}")
    print(f"[POLICY] Hard failures: {len(hard_failures)}")
    print(f"[POLICY] Soft warnings: {len(soft_warnings)}")

    return eligible, hard_failures, soft_warnings, explanation
