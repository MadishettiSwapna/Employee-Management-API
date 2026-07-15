from datetime import timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = "sqlite:///employee.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY")

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)