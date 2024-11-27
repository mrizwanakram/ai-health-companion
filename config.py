from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
