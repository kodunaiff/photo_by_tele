import os

import requests

if not os.path.exists('images'):
    os.makedirs('images')


def download_image(url, save_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)


link = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
save_path = os.path.join('images', 'hubble.jpeg')

download_image(link, save_path)
