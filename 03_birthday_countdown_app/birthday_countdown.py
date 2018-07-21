import datetime


def print_header():
	print('---------------------------------')
	print('      BIRTHDAY COUNTDOWN')
	print('---------------------------------')


def get_birthday_from_user():
	year = input('Year [YYYY]: ')
	month = input('Month [MM]: ')
	day = input('Day [DD]: ')

	return datetime.date(year=int(year), month=int(month), day=int(day))


def compute_days_between_dates(birthday, now):
	this_year = datetime.date(year=now.year, month=birthday.month, day=birthday.day)

	return (this_year - now).days


def print_birthday_information(number_of_days):
	if number_of_days < 0:
		print(f'You had your birthday {-number_of_days} days ago this year.')
	elif number_of_days > 0:
		print(f'Your birthday is in {number_of_days} days!')
	else:
		print('Happy birthday!!!')


def main():
	print_header()
	birthday = get_birthday_from_user()
	now = datetime.date.today()
	number_of_days = compute_days_between_dates(birthday, now)
	print_birthday_information(number_of_days)


if __name__ == '__main__':
	main()
