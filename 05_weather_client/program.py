import collections

import bs4
import requests


WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


def print_the_header():
    print('-------------------------------')
    print('          WEATHER APP')
    print('-------------------------------')
    print()


def get_html_from_web(zipcode):
    url = f'https://www.wunderground.com/weather/{zipcode}'
    response = requests.get(url)
    return response.text  # html


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # $('city-header h1').innerText
    # $('.condition-icon p').innerText
    # $('.condition-data .wu-value').innerText
    loc = soup.find('city-header').find('h1').get_text().strip()
    condition = soup.find(class_='condition-icon').find('p').get_text().strip()
    temp = soup.find(class_='condition-data').find(class_='wu-value').get_text().strip()
    scale = soup.find(class_='condition-data').find(class_='wu-label').get_text().strip()  # Fahrenheit

    return WeatherReport(condition, temp, scale, loc)


def main():
    print_the_header()
    zipcode = input('What zipcode do you want the weather for (97201)? ')
    html = get_html_from_web(zipcode)
    report = get_weather_from_html(html)
    print(f'The temperature in {report.loc} is {report.temp} °{report.scale} and {report.cond}')


if __name__ == '__main__':
    main()
