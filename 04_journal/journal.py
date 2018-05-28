import json
import os


def load(name):
    """
    Creates and loads a new journal.

    :param name: Name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename, 'r') as fin:
            return json.load(fin)

    return []


def save(name, journal_data):
    filename = get_full_pathname(name)
    with open(filename, 'w') as fout:
        json.dump(journal_data, fout)


def get_full_pathname(name):
    return os.path.abspath(os.path.join('./journals/', f'{name}.jrl'))


def add_entry(text, journal_data):
    journal_data.append(text)
