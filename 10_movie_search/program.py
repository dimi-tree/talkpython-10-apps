import requests.exceptions

import movie_svc


def print_the_header():
    app_header = 'MOVIE SEARCH APP'
    print('-' * (20 + len(app_header)))
    print(' ' * 10 + app_header)
    print('-' * (20 + len(app_header)))
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ').strip()

            if search != 'x':
                results = movie_svc.find_movies(search)
                print(f'Found {len(results):,} results.')
                for r in results:
                    print(f'{r.year} -- {r.title}')
                print()
        except ValueError:
            print('Error: Search text is required')
        except requests.exceptions.ConnectionError:
            print('Error: Your network is down.')
        except Exception as e:
            print(f'Unexpected error. Details: {e}')

    print('Exiting...')


def main():
    print_the_header()
    search_event_loop()


if __name__ == '__main__':
    main()
