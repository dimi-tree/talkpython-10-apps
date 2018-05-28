import os
import shutil

import requests


def save_image(name, folder, data):
    filename = os.path.join(folder, f'{name}.jpg')
    with open(filename, 'wb') as fout:
        shutil.copyfileobj(data, fout)


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = requests.get(url, stream=True).raw  # Binary
    save_image(name, folder, data)
    return None
