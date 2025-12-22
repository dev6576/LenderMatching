from pydantic import BaseModel
from uuid import UUID


class UnderwritingRunRequest(BaseModel):
    application_id: UUID


class UnderwritingRunResponse(BaseModel):
    run_id: UUID
    status: str


class UnderwritingStatusResponse(BaseModel):
    run_id: UUID
    status: str
    completed_lenders: int
    total_lenders: int
