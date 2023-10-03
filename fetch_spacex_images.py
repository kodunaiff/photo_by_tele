import argparse
import os

import requests
from get_file_extension_image import save_image


def fetch_spacex_last_launch(id):
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    response.raise_for_status()
    flickr_links = response.json()['links']['flickr']['original']
    for link_number, link in enumerate(flickr_links, start=1):
        save_path = os.path.join('images', f'space{link_number}.jpg')
        save_image(save_path, link)


def main():
    parser = argparse.ArgumentParser(
        description='Скрипт скачивает фотографии запуска ракет'
    )
    parser.add_argument('id', help='give me id')
    args = parser.parse_args()

    fetch_spacex_last_launch(args.id)


if __name__ == "__main__":
    main()
