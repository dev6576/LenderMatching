from app.rules.fico import FicoRule
from app.rules.time_in_business import TimeInBusinessRule
from app.rules.geography import GeographyRule

RULE_REGISTRY = {
    "min_fico": FicoRule,
    "min_time_in_business": TimeInBusinessRule,
    "allowed_states": GeographyRule,
}


def build_rule(rule_data: dict):
    rule_type = rule_data["rule_type"]
    rule_cls = RULE_REGISTRY.get(rule_type)

    if not rule_cls:
        raise ValueError(f"Unsupported rule type: {rule_type}")

    return rule_cls(
        operator=rule_data["operator"],
        value=rule_data["value"],
        weight=rule_data.get("weight", 0)
    )
