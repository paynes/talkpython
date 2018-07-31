import requests
import collections


MovieResult = collections.namedtuple('MovieResult', 'rating, imdb_code, title, director, duration, year, imdb_score, '
													'keywords, genres')


def find_movies(search):
	if not search or not search.strip():
		raise ValueError('Search text is required.')

	url = f'http://movie_service.talkpython.fm/api/search/{search}'
	resp = requests.get(url)
	resp.raise_for_status()

	movie_data = resp.json()
	movies_list = movie_data.get('hits')

	movies = [MovieResult(**md) for md in movies_list]

	movies.sort(key=lambda x: -x.year)

	return movies
