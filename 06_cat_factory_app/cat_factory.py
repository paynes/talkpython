import platform
import subprocess

import os
import cat_service


def main():
	print_header()

	folder = get_or_create_output_folder()
	print(f'Found or created folder: {folder}')

	download_cats(folder)
	display_cats(folder)


def print_header():
	print('---------------------------')
	print('      CAT FACTORY APP')
	print('---------------------------')


def get_or_create_output_folder():
	folder = 'cat_pictures'

	base_path = os.path.dirname(__file__)
	full_path = os.path.join(base_path, folder)

	if not os.path.exists(full_path) or not os.path.isdir(full_path):
		print(f'Creating new directory at {full_path}')
		os.mkdir(full_path)

	return full_path


def download_cats(folder):
	print('Contacting server to download cats...')
	for i in range(1, 9):
		name = f'lolcat_{i}'
		print(f'Downloading cat {name}')
		cat_service.get_cat(folder, name)

	print('Done.')


def display_cats(folder):
	if platform.system() == 'Darwin':
		subprocess.call(['open', folder])
	elif platform.system() == 'Linux':
		subprocess.call(['xdg-open', folder])
	elif platform.system() == 'Windows':
		subprocess.call(['explorer', folder])


if __name__ == '__main__':
	main()
