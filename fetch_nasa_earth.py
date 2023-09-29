import os

import requests

from get_file_extension_image import save_image


def main():
    params = {
        'api_key': 'DEMO_KEY'
    }
    url_ex = 'https://api.nasa.gov/EPIC/api/natural/images'

    response = requests.get(url_ex, params=params)
    response.raise_for_status()
    epic_data = response.json()
    for epic_number, epic_record in enumerate(epic_data):
        date_image, time_image = epic_record['date'].split()
        year, month, day = date_image.split('-')
        name_image = epic_record['image']
        save_path = os.path.join('images', f'earth_picture{epic_number + 1}.png')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}' \
              f'/{day}/'f'png/{name_image}.png'
        response = requests.get(url, params=params)
        response.raise_for_status()
        image_url = response.url
        save_image(save_path, image_url)


if __name__ == "__main__":
    main()
