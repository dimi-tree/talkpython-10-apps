from operator import attrgetter

import collections
import requests

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres')


def find_movies(search_text):

    if search_text is None or not search_text.strip():
        raise ValueError('search_text is required')

    url = f'http://movie_service.talkpython.fm/api/search/{search_text}'

    resp = requests.get(url)
    resp.raise_for_status()

    return sorted(
        (MovieResult(**movie_data) for movie_data in resp.json().get('hits')),
        key=attrgetter('year'),
        reverse=True)
