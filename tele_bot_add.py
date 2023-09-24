import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def published_picture(delay):
    while True:
        random.shuffle(files_in_dir)
        for file_pic in files_in_dir:
            time.sleep(int(delay))
            bot.send_document(chat_id=chat_id,
                              document=open('images/' + f'{file_pic}', 'rb'))


load_dotenv()
token = os.getenv('token_tele')

bot = telegram.Bot(token=token)
updates = bot.get_updates()
chat_id = '@space_pictures03'
path_picture = 'images/'
files_in_dir = os.listdir(path_picture)


def get_delay():
    parser = argparse.ArgumentParser(
        description='Получает частоту публикаций'
    )
    parser.add_argument(
        '-t',
        '--delay_time',
        help='give me time_delay',
        type=int,
        default=int(os.getenv('DELAY_TIME', 14400))
    )
    args = parser.parse_args()
    return args.delay_time


delay = get_delay()
published_picture(delay)
