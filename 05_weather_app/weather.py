import requests
import bs4

def main():
	print_header()

	zip_code = input('What zipcode do you want the wheather for (97201)? ')
	html = get_html_from_web(zipcode=zip_code)

	get_weather_from_html(html)


def print_header():
	print('--------------------------------')
	print('         WEATHER APP')
	print('--------------------------------')


def get_html_from_web(zipcode):
	url = f'http://www.wunderground.com/wheather-forecast/{zipcode}'
	return requests.get(url=url).text


def get_weather_from_html(html):
	soup = bs4.BeautifulSoup(html)
	print(soup)


if __name__ == '__main__':
	main()
