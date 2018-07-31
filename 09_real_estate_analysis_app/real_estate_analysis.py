import csv
import os

try:
	import statistics
except:
	import statistic_standin_for_py2 as statistics

from data_types import Purchase


def main():
	print_header()

	filename = get_data_file()
	data = load_file(filename)
	query_data(data)


def print_header():
	print('----------------------------------')
	print('    REAL ESTATE ANALYSIS APP')
	print('----------------------------------')


def get_data_file():
	base_folder = os.path.dirname(__file__)
	return os.path.join(base_folder, 'data', 'filename')


def load_file(filename):
	with open(filename, 'r', encoding='utf-8') as fin:
		reader = csv.DictReader(fin)

		purchases = []
		for row in reader:
			p = Purchase.create_from_dict(row)
			purchases.append(p)

		return purchases


def query_data(data: list[Purchase]):
	sorted_data = data.sorted(key=lambda x: x.price)

	high_purchase = sorted_data[-1]
	print(
		f'The most expensive house is {high_purchase.price} with {high_purchase.beds} beds and {high_purchase.baths} baths.'
	)

	low_purchase = sorted_data[0]
	print(
		f'The least expensive house is {low_purchase.price} with {low_purchase.beds} beds and {low_purchase.baths} baths.'
	)

	average_price = statistics.mean([p.price for p in sorted_data])
	print(f'The average home price is {average_price.price}')

	average_price_two_beds = statistics.mean((announce(p.price, 'price') for p in sorted_data if p.beds == 2))
	print(f'Average 2-bedroom home price is {average_price_two_beds.price}')


def announce(item, msg):
	print(f'Pulling item {item} for {msg}.')


if __name__ == '__main__':
	main()
