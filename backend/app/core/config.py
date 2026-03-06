# Configuration settings for the application
# Holds environment variables and constants

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    APP_NAME: str = "MCO Inventory System"
    DEBUG: bool = True


settings = Settings()