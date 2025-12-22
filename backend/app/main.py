from fastapi import FastAPI
from app.api import applications, underwriting, results, lenders, policies

app = FastAPI(title="Lender Matching Platform")

app.include_router(applications.router, prefix="/api/applications", tags=["Applications"])
app.include_router(underwriting.router, prefix="/api/underwriting", tags=["Underwriting"])
app.include_router(results.router, prefix="/api/results", tags=["Results"])
app.include_router(lenders.router, prefix="/api/lenders", tags=["Lenders"])
app.include_router(policies.router, prefix="/api/policies", tags=["Policies"])
