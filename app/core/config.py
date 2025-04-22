import os
from pathlib import Path
from dotenv import load_dotenv

# ----------------------------
# ENVIRONMENT CONFIGURATION
# ----------------------------

# Determine the absolute path to the project root (3 levels up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Build full path to the .env file located in the root directory
env_path = BASE_DIR / ".env"

# Load the .env file so os.getenv(...) can access its contents
load_dotenv(dotenv_path=env_path)


# ----------------------------
# APPLICATION SETTINGS CLASS
# ----------------------------

class Settings:
    """
    Application settings loaded from environment variables.

    Add additional environment configs here as needed (e.g., DB_URL, LOG_LEVEL).
    """
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.5"))


# Create a single instance of settings to be imported throughout the app
settings = Settings()
