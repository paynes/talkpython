import os
import requests
import shutil


def get_cat(folder, name):
	url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
	data = get_data_from_url(url)
	save_image(folder, name, data)


def get_data_from_url(url):
	return requests.get(url, stream=True).raw


def save_image(folder, name, data):
	file_name = os.path.join(folder, name + '.jpg')
	with open(file_name, 'wb') as out:
		shutil.copyfileobj(data, out)
