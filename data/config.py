import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

GROUP_ID = str(os.getenv("GROUP_ID"))

IP = os.getenv("IP")
POSTGRES_USER = str(os.getenv("POSTGRES_USER"))
POSTGRES_PASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

ALLOW_GIFS = os.getenv("ALLOW_GIFS", False) in ["True", "true", "1"]
SOURCE_URL = os.getenv("SOURCE_URL", "https://github.com/profectus200/inno2ch-bot")


POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{IP}/{DATABASE}"