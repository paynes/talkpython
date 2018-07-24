import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatheReport', 'cond, temp, scale, loc')


def main():
	print_header()

	zip_code = input('What zipcode do you want the wheather for (97201)? ')
	html = get_html_from_web(zipcode=zip_code)

	report = get_weather_from_html(html)

	print(f'The temp in {report.loc} is {report.cond} and {report.temp} {report.scale}')


def print_header():
	print('--------------------------------')
	print('         WEATHER APP')
	print('--------------------------------')


def get_html_from_web(zipcode):
	url = f'http://www.wunderground.com/weather-forecast/{zipcode}'
	return requests.get(url=url).text


def get_weather_from_html(html):
	soup = bs4.BeautifulSoup(html, 'html.parser')

	loc = soup.find(class_='city-header').find('h1').get_text()
	condition = soup.find(class_='city-conditions').find(class_='conditions-extra').find('p').get_text()
	temp = soup.find(class_='city-conditions').find(class_='current-temp').find(class_='wu-value').get_text()
	scale = soup.find(class_='city-conditions').find(class_='current-temp').find(class_='wu-label').get_text()

	loc = cleanup_text(loc)
	condition = cleanup_text(condition)
	temp = cleanup_text(temp)
	scale = cleanup_text(scale)

	return WeatherReport(condition, temp, scale, loc)


def find_city_and_state_from_location(loc: str):
	return loc.split('\n')[0]


def cleanup_text(text: str):
	if not text:
		return text

	return text.strip()

if __name__ == '__main__':
	main()
