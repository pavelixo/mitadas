from pathlib import Path
from os import getenv
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent

load_dotenv(
    BASE_DIR / ".env"
)

load_dotenv(
    BASE_DIR / ".env.example", 
    override=False
)

TOKEN = getenv("TOKEN")
DATABASE = getenv("DATABASE")