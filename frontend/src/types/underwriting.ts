export interface LoanApplication {
  credit_score: number
  years_in_business: number
  loan_amount: number
}

export interface RuleExplanation {
  rule_type: string
  operator: string
  expected: any
  actual: any
  result: string
  hard_rule: boolean
}

export interface LenderResult {
  lender_id: string
  policy_id: string
  eligible: boolean
  hard_failures: RuleExplanation[]
  soft_warnings: RuleExplanation[]
  explanation: RuleExplanation[]
  llm_explanation: string
}

export interface UnderwritingResponse {
  eligible_lenders: LenderResult[]
  rejected_lenders: LenderResult[]
}
