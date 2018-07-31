import movie_svc
from requests.exceptions import ConnectionError


def main():
	print_header()
	search_event_loop()


def print_header():
	print('-------------------------------------')
	print('          MOVIE SEARCH APP')
	print('-------------------------------------')


def search_event_loop():
	search = 'ONCE_THROUGH_LOOP'
	while search != 'x':
		try:
			search = input('Movie search text (x to exit): \n')
			if search != 'x':
				results = movie_svc.find_movies(search)
				print(f'Found {len(results)}')
				for r in results:
					print(f'{r.year} ---  {r.title}')

		except ValueError:
			print(f'Error: Search text is required.')
		except ConnectionError:
			print(f'Error: Your network is down.')
		except Exception as x:
			print(f'Unexpected error. Details: {x}')

	print('Exiting...')

if __name__ == '__main__':
	main()
