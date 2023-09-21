import argparse
import os

import requests
from dotenv import load_dotenv

from space_x_im import get_file_extension


def fetch_nasa_apod(count_image):
    token = os.getenv('token')
    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': f'{count_image}',
        'api_key': f'{token}',
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    nasa_pic = response.json()
    for link_number, link in enumerate(nasa_pic):
        response = requests.get(link['url'])
        response.raise_for_status()
        form = get_file_extension(link['url'])
        save_path = os.path.join('images', 'nasa_apod'
                                 + str(link_number + 1) + str(form))
        with open(save_path, 'wb') as file:
            file.write(response.content)


load_dotenv()
parser = argparse.ArgumentParser(
    description='Получает количество картинок'
)
parser.add_argument('count_image', help='give me count')
args = parser.parse_args()

fetch_nasa_apod(args.count_image)
