from pydantic import BaseModel
from uuid import UUID

class LenderOut(BaseModel):
    lender_id: UUID
    name: str

    class Config:
        orm_mode = True
