import json
from app.llm.schemas import LLMRuleExtraction


def parse_llm_output(raw: str) -> LLMRuleExtraction:
    try:
        parsed = json.loads(raw)
        return parsed
    except Exception as e:
        raise ValueError(f"Invalid LLM output: {e}")
