import argparse
import os

import requests
from dotenv import load_dotenv

from get_file_extension_image import get_file_extension, save_image


def fetch_nasa_apod(count_image, token):
    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': f'{count_image}',
        'api_key': f'{token}',
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    nasa_pictures = response.json()
    for link_number, link in enumerate(nasa_pictures):
        form = get_file_extension(link['url'])
        save_path = os.path.join('images', f'nasa_apod{link_number + 1}{form}')
        save_image(save_path, link['url'])


def main():
    load_dotenv()
    token = os.getenv('TOKEN_NASA')
    parser = argparse.ArgumentParser(
        description='Скачивает популярные изображения космоса'
    )
    parser.add_argument('count_image', help='give me count')
    args = parser.parse_args()

    fetch_nasa_apod(args.count_image, token)


if __name__ == "__main__":
    main()
