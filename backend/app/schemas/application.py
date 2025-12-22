from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class BorrowerSchema(BaseModel):
    business_name: str
    industry: str
    state: str
    years_in_business: int
    annual_revenue: Optional[float]


class GuarantorSchema(BaseModel):
    fico_score: int = Field(..., ge=300, le=850)


class LoanRequestSchema(BaseModel):
    amount: float
    term_months: int
    equipment_type: str
    equipment_age_months: Optional[int]


class ApplicationCreateRequest(BaseModel):
    borrower: BorrowerSchema
    guarantor: GuarantorSchema
    loan: LoanRequestSchema


class ApplicationResponse(BaseModel):
    application_id: UUID
    status: str
