import journal_utils


def main():
	print_header()
	run_event_loop()


def print_header():
	print('-----------------------------------')
	print('           JOURNAL APP')
	print('-----------------------------------')


def run_event_loop():
	print('What do you want to do with your journal?')

	cmd = 'EMPTY'

	journal_name = 'default'
	journal_data = journal_utils.load(journal_name)

	while cmd != 'x' and cmd:
		cmd = input('[L]ist entries, [A]dd an entry, E[x]it \n')
		cmd = cmd.lower().strip()

		if cmd == 'l':
			list_entries(journal_data)
		elif cmd == 'a':
			add_entry(journal_data)
		elif cmd != 'x' and cmd:
			print(f'Sorry {cmd} is unknown command.')

	journal_utils.save(journal_name, journal_data)


def list_entries(data):
	print('Entries: \n')
	for index, entry in enumerate(reversed(data)):
		print(f'{index + 1}: {entry}')


def add_entry(data):
	entry = input('Type your entry: ')
	journal_utils.add_entry(entry, data)


if __name__ == '__main__':
	main()
