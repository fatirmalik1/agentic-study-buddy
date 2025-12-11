import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "Groq")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama-3.1-8b-instant")
    DEFAULT_PERSONA = os.getenv("DEFAULT_PERSONA", "Friendly Tutor")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.9"))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))


settings = Settings()