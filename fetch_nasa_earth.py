import os

import requests

url_ex = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'

response = requests.get(url_ex)
response.raise_for_status()
earth_db = response.json()
for epic_number, epic_e in enumerate(earth_db):
    date_e, time_e = epic_e['date'].split()
    year, month, day = date_e.split('-')
    name_image = epic_e['image'] + '.png'
    save_path = os.path.join('images', 'earth_pic'
                             + str(epic_number + 1) + '.png')
    url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/' \
          f'png/{name_image}?api_key=DEMO_KEY'
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)
