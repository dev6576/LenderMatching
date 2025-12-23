import logging
import requests

from app.llm.config import (
    GROQ_API_KEY,
    GROQ_API_URL,
    GROQ_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
    TIMEOUT_SECONDS,
)

logger = logging.getLogger(__name__)


class LLMAuthError(RuntimeError):
    pass


class LLMCallError(RuntimeError):
    pass


def call_llm(prompt: str) -> str:
    if not GROQ_API_KEY:
        raise LLMAuthError("GROQ_API_KEY is not set or not loaded")

    logger.info("Making LLM call with prompt length: %d", len(prompt))

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a cautious underwriting policy analyst. "
                           "Return ONLY valid JSON. No explanations.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }

    try:
        response = requests.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=TIMEOUT_SECONDS,
        )
    except requests.RequestException as e:
        logger.exception("Failed to reach Groq API")
        raise LLMCallError(f"LLM request failed: {e}")

    logger.info("LLM API response status: %s", response.status_code)

    if response.status_code == 401:
        raise LLMAuthError("Unauthorized (401): invalid or missing GROQ_API_KEY")

    if not response.ok:
        logger.error("LLM API error response: %s", response.text)
        raise LLMCallError(
            f"LLM API error {response.status_code}: {response.text}"
        )

    try:
        data = response.json()
    except ValueError as e:
        logger.error("Invalid JSON from LLM: %s", response.text)
        raise LLMCallError("LLM returned non-JSON response")

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as e:
        logger.error("Unexpected LLM response shape: %s", data)
        raise LLMCallError("Unexpected LLM response format")
