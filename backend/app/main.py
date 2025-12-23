from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from app.api import applications, underwriting, results, lenders, policies, rules

app = FastAPI(title="Lender Matching Platform")

# Test logging
logger = logging.getLogger(__name__)
logger.info("Server starting up...")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(applications.router, prefix="/api/v1/applications", tags=["Applications"])
app.include_router(underwriting.router, prefix="/api/v1/underwriting", tags=["Underwriting"])
app.include_router(results.router, prefix="/api/v1/results", tags=["Results"])
app.include_router(lenders.router, prefix="/api/v1/lenders", tags=["Lenders"])
app.include_router(policies.router, tags=["Policies"])
app.include_router(rules.router, tags=["Rules"])
