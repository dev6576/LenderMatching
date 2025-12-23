import logging
from app.llm.client import call_llm
from app.llm.prompts import EXTRACT_RULES_PROMPT
from app.llm.parser import parse_llm_output
import json,re
import sys

logger = logging.getLogger(__name__)


def extract_rules_from_document(document_text: str):
    logger.info("DEBUG: Starting extract_rules_from_document")
    logger.info(f"Extracting rules from document text of length {len(document_text)}")
    logger.info(f"DEBUG: document_text length: {len(document_text)}")
    
    prompt = EXTRACT_RULES_PROMPT.format(document_text=document_text)
    logger.info("Generated prompt for LLM:")
    logger.info(prompt)
    logger.info("="*50)
    
    try:
        raw_output = call_llm(prompt)
        logger.info(f"Raw LLM Response:")
        logger.info(raw_output)
        logger.info("="*50)
        logger.info(f"Received raw output from LLM, length: {len(raw_output)}")
    except Exception as e:
        logger.error(f"Failed to call LLM: {e}")
        raise
    
    try:
        parsed_result = parse_llm_output(raw_output)
        logger.info(f"Parsed Result:")
        logger.info(json.dumps(parsed_result, indent=2))
        logger.info("="*50)
        logger.info(f"Successfully parsed LLM output into {len(parsed_result.get('rules', []))} rules")
        return parsed_result
    except Exception as e:
        logger.error(f"Failed to parse LLM output: {e}")
        raise
