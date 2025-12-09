from typing import Optional

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from src.common.custom_exception import CustomException
from src.config.settings import settings


def get_llm(provider: str, model_name: str, temperature: Optional[float] = None):
    """
    Return a configured chat LLM for the requested provider and model.
    """
    normalized_provider = provider.strip().lower()
    temp = temperature if temperature is not None else settings.TEMPERATURE

    if normalized_provider == "openai":
        if not settings.OPENAI_API_KEY:
            raise CustomException("OpenAI API key is not configured.")
        return ChatOpenAI(
            model=model_name,
            openai_api_key=settings.OPENAI_API_KEY,
            temperature=temp,
        )

    if normalized_provider == "groq":
        if not settings.GROQ_API_KEY:
            raise CustomException("Groq API key is not configured.")
        return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=model_name,
            temperature=temp,
        )

    raise CustomException(f"Unsupported provider '{provider}'.")

