"""
Synchronous policy ingestion workflow.

NOTE:
This is intentionally written as a simple orchestration layer.
It can later be converted to an async / Hatchet-based workflow
without changing business logic.
"""

import logging
from app.services.pdf_extractor import extract_pdf_text
from app.llm.service import extract_rules_from_document
from app.services.policy_persistence import persist_policy_draft

logger = logging.getLogger(__name__)


def ingest_policy_document(
    lender_id: str,
    pdf_path: str,
) -> str:
    logger.info(f"Starting policy ingestion for lender {lender_id} with PDF {pdf_path}")
    
    # Step 1: extract raw text
    logger.info("Step 1: Extracting text from PDF")
    try:
        document_text = extract_pdf_text(pdf_path)
        logger.info(f"Successfully extracted {len(document_text)} characters from PDF")
    except Exception as e:
        logger.error(f"Failed to extract text from PDF: {e}")
        raise
    
    # Step 2: extract rules via LLM
    logger.info("Step 2: Extracting rules via LLM")
    try:
        llm_result = extract_rules_from_document(document_text)
        logger.info(f"Successfully extracted rules: {len(llm_result.get('rules', []))} rules found")
    except Exception as e:
        logger.error(f"Failed to extract rules via LLM: {e}")
        raise
    
    # Step 3: persist policy + rules
    logger.info("Step 3: Persisting policy draft")
    try:
        policy_id = persist_policy_draft(
            lender_id=lender_id,
            raw_text=document_text,
            llm_result=llm_result,
        )
        logger.info(f"Successfully persisted policy with ID {policy_id}")
    except Exception as e:
        logger.error(f"Failed to persist policy draft: {e}")
        raise
    
    logger.info(f"Policy ingestion completed successfully for lender {lender_id}, policy ID: {policy_id}")
    return policy_id
