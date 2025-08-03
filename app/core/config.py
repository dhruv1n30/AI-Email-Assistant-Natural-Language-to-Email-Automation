# Application settings and environment variables
import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY : str = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY: str = os.getenv("GEMINI_API_KEY")

