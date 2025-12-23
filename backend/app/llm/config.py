import os
from dotenv import load_dotenv

# Load environment variables once
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "openai/gpt-oss-120b"

TEMPERATURE = 0.2
MAX_TOKENS = 1500
TIMEOUT_SECONDS = 30
