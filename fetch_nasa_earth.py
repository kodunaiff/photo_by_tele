import os

import requests
from dotenv import load_dotenv

from get_file_extension_image import save_image


def main():
    load_dotenv()
    nasa_token = os.environ['TOKEN_NASA']
    params = {
        'api_key': nasa_token
    }
    url_ex = 'https://api.nasa.gov/EPIC/api/natural/images'

    response = requests.get(url_ex, params=params)
    response.raise_for_status()
    epic_images = response.json()
    for epic_number, epic_record in enumerate(epic_images, start=1):
        image_date, image_time = epic_record['date'].split()
        year, month, day = image_date.split('-')
        image_name = epic_record['image']
        save_path = os.path.join('images', f'earth_picture{epic_number}.png')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}' \
              f'/{day}/'f'png/{image_name}.png'
        save_image(save_path, url, nasa_token)


if __name__ == "__main__":
    main()
