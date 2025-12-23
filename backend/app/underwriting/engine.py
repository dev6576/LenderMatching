from typing import Any

def evaluate_rule(rule, application: dict) -> dict:
    rule_type = rule.rule_type
    operator = rule.operator
    expected = rule.value

    actual = application.get(rule_type)

    if actual is None:
        return {
            "passed": False,
            "explanation": f"Missing required field: {rule_type}",
        }

    passed = False

    if operator == ">=":
        passed = actual >= expected
    elif operator == ">":
        passed = actual > expected
    elif operator == "<=":
        passed = actual <= expected
    elif operator == "<":
        passed = actual < expected
    elif operator == "==":
        passed = actual == expected
    else:
        return {
            "passed": False,
            "explanation": f"Unsupported operator: {operator}",
        }

    explanation = (
        f"{rule_type} check passed"
        if passed
        else f"{rule_type} check failed: {actual} {operator} {expected}"
    )

    return {
        "passed": passed,
        "explanation": explanation,
    }
