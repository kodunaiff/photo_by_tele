import argparse
import os
import random
import time

import telegram
from dotenv import load_dotenv


def post_images(delay, chat_id, files_in_dir, bot):
    while True:
        random.shuffle(files_in_dir)
        for picture in files_in_dir:
            time.sleep(int(delay))
            with open(f'images/{picture}', 'rb') as picture:
                bot.send_document(chat_id=chat_id, document=picture)


def get_delay(delay_time):
    parser = argparse.ArgumentParser(
        description='Публикует фотографии в ТГ'
    )
    parser.add_argument(
        '-t',
        '--delay_time',
        help='give me time_delay',
        type=int,
        default=delay_time
    )
    args = parser.parse_args()
    return args.delay_time


def main():
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=token)
    delay_time = os.getenv('DELAY_TIME')
    chat_id = os.getenv('TG_CHAT_ID')
    path_picture = 'images/'
    files_in_dir = os.listdir(path_picture)
    delay = get_delay(delay_time)
    post_images(delay, chat_id, files_in_dir, bot)


if __name__ == "__main__":
    main()
