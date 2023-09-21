import argparse
import os

import requests


def fetch_spacex_last_launch(id):
    url = f'https://api.spacexdata.com/v5/launches/{id}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    flickr_links = data['links']['flickr']['original']
    for link_number, link in enumerate(flickr_links):
        response = requests.get(link)
        response.raise_for_status()
        save_path = os.path.join('images',
                                 'space' + str(link_number + 1) + '.jpg')
        with open(save_path, 'wb') as file:
            file.write(response.content)


parser = argparse.ArgumentParser(
    description='Получает id запуска'
)
parser.add_argument('id', help='give me id')
args = parser.parse_args()

fetch_spacex_last_launch(args.id)
