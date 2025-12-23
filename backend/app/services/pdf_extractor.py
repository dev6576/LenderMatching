import pdfplumber
import logging

logger = logging.getLogger(__name__)


def extract_pdf_text(pdf_path: str) -> str:
    logger.info(f"Extracting text from PDF: {pdf_path}")
    pages = []

    try:
        with pdfplumber.open(pdf_path) as pdf:
            logger.info(f"PDF has {len(pdf.pages)} pages")
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    pages.append(text)
                    logger.debug(f"Extracted text from page {i+1}")
                else:
                    logger.warning(f"No text found on page {i+1}")
        
        extracted_text = "\n".join(pages)
        logger.info(f"Successfully extracted {len(extracted_text)} characters from {len(pages)} pages")
        return extracted_text
    except Exception as e:
        logger.error(f"Failed to extract text from PDF {pdf_path}: {e}")
        raise
