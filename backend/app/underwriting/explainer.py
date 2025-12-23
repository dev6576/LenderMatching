from app.llm.client import call_llm
import json


def generate_underwriting_explanation(
    lender_id: str,
    eligible: bool,
    hard_failures,
    soft_warnings,
):
    """
    Uses LLM to generate a human-readable explanation
    based on deterministic evaluation output.
    """

    prompt = f"""
You are an underwriting analyst.

Given the following evaluation result, explain in plain English
why the application was accepted or rejected.

Lender ID: {lender_id}
Eligibility: {"ELIGIBLE" if eligible else "REJECTED"}

Hard Failures:
{json.dumps([hf.dict() for hf in hard_failures], indent=2)}

Soft Warnings:
{json.dumps([sw.dict() for sw in soft_warnings], indent=2)}

Write a concise explanation suitable for an applicant or broker.
Do not invent new rules.
"""

    print("[LLM] Generating underwriting explanation")

    explanation = call_llm(prompt)

    print("[LLM] Explanation generated")

    return explanation
