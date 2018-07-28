import collections
import os


SearchResult = collections.namedtuple('SearchResult', 'file, line_number, text')


def main():
	print_header()
	folder = get_folder_from_user()

	if not folder:
		print("Sorry we can't search that location")
		return

	text = get_search_text_from_user()

	matches = search_folders(folder, text)
	for match in matches:
		print('-----MATCH-----')
		print(f'file: {match.file}')
		print(f'line number: {match.line_number}')
		print(f'text: {match.text.strip()}')
		print()


def print_header():
	print('-----------------------------')
	print('      FILE SEARCH APP')
	print('-----------------------------')


def get_folder_from_user():
	folder = input('What folder do you want to search? ')
	if not folder or not folder.strip():
		return None

	if not os.path.isdir(folder):
		return None

	return os.path.abspath(folder)


def get_search_text_from_user():
	return input('What are you searching for [single phrases only]? ')


def search_folders(folder, text):
	items = os.listdir(folder)

	for item in items:
		full_item = os.path.join(folder, item)
		if os.path.isdir(full_item):
			yield from search_folders(full_item, text)
		else:
			yield from search_file(full_item, text)


def search_file(filename, search_text):
	with open(filename, 'r', encoding='utf-8') as fin:
		for line_number, line in enumerate(fin, 1):
			if line.lower().find(search_text) >= 0:
				yield SearchResult(line_number=line_number, file=filename, text=line)


if __name__ == '__main__':
	main()
