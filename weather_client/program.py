import requests
import bs4


def main():
    print_header()
    zipcode = get_zipcode_from_user()
    html = get_html_from_web(zipcode)
    get_weather_from_html(html)
    # display forecast


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
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature.wu-label'
    # weatherTempCss = '.wu-unit-temperature.wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')


if __name__ == '__main__':
    main()
