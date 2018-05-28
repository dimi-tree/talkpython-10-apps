import collections
import glob
import os


SearchResult = collections.namedtuple('SearchResult', 'file, line, text')


def print_the_header():
    app_header = 'FILE SEARCH APP'
    print('-' * (20 + len(app_header)))
    print(' ' * 10 + app_header)
    print('-' * (20 + len(app_header)))
    print()


def get_folder_from_user():
    folder = os.path.expanduser(input('What folder do you want to search? ').strip())
    if not folder:
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrase only]? ').strip()
    return text.lower()


def search_file(filename, search_text):

    # NOTE: by specifying the encoding we are making an assumption that the filename is a text file
    with open(filename, 'r', encoding='utf-8') as fin:

        for line_num, line in enumerate(fin):
            if line.lower().find(search_text) >= 0:
                yield SearchResult(file=filename, line=line_num, text=line.strip())


def search_folders(folder, text):
    all_matches = []
    items = glob.glob(os.path.join(folder, '*'))

    for item in items:
        if os.path.isdir(item):
            yield from search_file(item, text)

            # yield from search_file(item, text)
            # where search_file is a generator (co-routine)
            #
            # is equivalent to
            #
            # for m in search_file(item, text)
            #     yield m
        else:
            yield from search_file(item, text)

    return all_matches


def main():
    print_the_header()

    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return

    for m in search_folders(folder, text):
        print('-' * 10, ' MATCH ', '-' * 10)
        print(f'file: {m.file}')
        print(f'line: {m.line}')
        print(f'match: {m.text}')
        print()


if __name__ == '__main__':
    main()
