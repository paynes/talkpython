import os


def load(name):
    """
    This method creates and load a new journal.

    :param name: This base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry)

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)

    with open(filename, 'w') as out:
        for entry in journal_data:
            out.write(entry + '\n')


def add_entry(entry, journal_data):
    journal_data.append(entry)


def get_full_pathname(name):
    return os.path.join('./journals/', name + '.jrl')
