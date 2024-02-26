import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URI = ""
BOT_TOKEN = str(os.getenv("TOKEN"))
