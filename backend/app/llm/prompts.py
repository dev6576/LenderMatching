EXTRACT_RULES_PROMPT = """
You are an underwriting policy analyst.

From the lender policy document below, extract eligibility rules.

Rules MUST follow this schema:
- rule_type: one of [credit_score, years_in_business, loan_amount, annual_revenue, monthly_cash_flow]
- operator: one of [>=, <=, >, <, ==]
- value: numeric
- hard_rule: true if mandatory, false if preference

Guidelines:
- Do NOT invent rules
- If conditional or ambiguous, include notes
- Ignore pricing, rates, legal text

Return JSON ONLY in this format:
{{
  "rules": [...],
  "assumptions": [...],
  "unmapped_sections": [...]
}}

DOCUMENT TEXT:
{document_text}
"""
