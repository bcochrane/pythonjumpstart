import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'condition, temperature, scale, location')


def main():
    print_header()
    zipcode = get_zipcode_from_user()
    html = get_html_from_web(zipcode)
    report = get_weather_from_html(html)
    print(f'The weather in {report.location}, {zipcode} is {report.condition} '
          f'and {report.temperature} degrees {report.scale}.')


def print_header():
    print('-----------------')
    print('   WEATHER APP')
    print('-----------------')
    print()


def get_zipcode_from_user():
    code = input('For what zip code would you like the weather forecast? ')
    return code


def get_html_from_web(code):
    url = f'http://www.wunderground.com/weather-forecast/{code}'
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temperature = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    location = clean_text(location)
    condition = clean_text(condition)
    temperature = clean_text(temperature)
    scale = clean_text(scale)

    report = WeatherReport(location=location, condition=condition,
                           temperature=temperature, scale=scale)
    return report


def clean_text(text: str):
    if text:
        text = text.strip()
    return text


if __name__ == '__main__':
    main()
