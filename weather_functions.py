import requests
from tabulate import tabulate


def convert_kelvin_to_celsius(kelvin_grades):
    return round((kelvin_grades - 273.15), 2)


def weather_api_response(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}\
        &appid=e23405c46081165114dee507b5b34191'
    response = requests.get(url)
    if (response.status_code == 200):
        return response.json()
    return response.status_code


def extract_temp_parameters(api_response, dict):
    temperature = {
        'temp': 'Current temp.',
        'feels_like': 'Feels like',
        'temp_min': 'Min. temp.',
        'temp_max': 'Max. temp.'}
    for k, v in api_response['main'].items():
        if k in temperature:
            dict[temperature[k]] = f'{convert_kelvin_to_celsius(v)}°C'


def extract_weather_parameters(api_response, dict):
    dict['City'] = api_response['name']
    dict['Weather conditions'] = api_response['weather'][0]['description']
    extract_temp_parameters(api_response, dict)
    dict['Humidity'] = f"{api_response['main']['humidity']}%"
    dict['Pressure'] = f"{api_response['main']['pressure']}"


def table_format(dict):
    return (tabulate([(k, v) for k, v in dict.items()], tablefmt="rst"))


def report_weather_conditions():
    results = {}
    api_response = weather_api_response(input('Type a city: '))
    extract_weather_parameters(api_response, results)
    return table_format(results)
