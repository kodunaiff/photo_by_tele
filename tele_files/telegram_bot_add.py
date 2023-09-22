import os

import telegram
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token_tele')

bot = telegram.Bot(token=token)
updates = bot.get_updates()
chat_id = '@space_pictures03'

bot.send_message(chat_id=chat_id, text="HI people.")
