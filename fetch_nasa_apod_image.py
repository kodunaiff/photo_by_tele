import argparse
import os

import requests
from dotenv import load_dotenv

from get_file_extension_image import get_file_extension, save_image


def fetch_nasa_apod(image_count, token):
    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': f'{image_count}',
        'api_key': f'{token}',
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    nasa_pictures = response.json()
    for link_number, link in enumerate(nasa_pictures, start=1):
        form = get_file_extension(link['url'])
        save_path = os.path.join('images', f'nasa_apod{link_number}{form}')
        save_image(save_path, link['url'])


def main():
    load_dotenv()
    nasa_token = os.getenv('TOKEN_NASA')
    parser = argparse.ArgumentParser(
        description='Скачивает популярные изображения космоса'
    )
    parser.add_argument('image_count', help='give me count')
    args = parser.parse_args()

    fetch_nasa_apod(args.image_count, nasa_token)


if __name__ == "__main__":
    main()
