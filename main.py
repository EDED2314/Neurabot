import interactions
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = interactions.Client(token=TOKEN)
