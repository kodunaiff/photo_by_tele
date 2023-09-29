import os
from urllib.parse import urlparse

import requests


def get_file_extension(url):
    parsed_url = urlparse(url)
    url = parsed_url.path
    filename, file_extension = os.path.splitext(url)
    return file_extension

def save_image(save_path, link):
    response = requests.get(link)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)

def main():
    url = "https://example.com/txt/hello%20world.txt?v=9#python"


if __name__ == "__main__":
    main()
