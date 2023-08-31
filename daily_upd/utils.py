import json
import requests
from decouple import config


API_KEY_1 = config('CURRENCYAPI_KEY')
API_ENDPOINT_1 = 'https://api.currencyapi.com/v3/latest'

API_KEY_2 = config('WEATHERAPI_KEY')
API_ENDPOINT_2 = "http://api.openweathermap.org/data/2.5/weather?"


def get_currencies() -> list:
    currency_codes = []
    with open('currency.json') as f:
        currency_data = json.load(f)
        for currency in currency_data:
            code, _ = list(currency.items())[0]
            currency_codes.append(code)
    return sorted(currency_codes)


def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    query_params = {
        'apikey': API_KEY_1,
        'base_currency': from_currency,
        'currencies': to_currency
    }
    response = requests.get(API_ENDPOINT_1, params=query_params)
    currency_data = response.json()
    exchange_rate = currency_data['data'][to_currency]['value']
    exchanged_value = exchange_rate * amount
    return exchanged_value


# Fetch today's weather from OpenWeatherAPI
def get_weather(city):

    complete_url = API_ENDPOINT_2 + "appid=" + API_KEY_2 + "&q=" + city
    response = requests.get(complete_url)

    x = response.json()
    y = x["main"]

    current_temperature = y["temp"] - 273.15 # convert to Celsius
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    
    z = x["weather"]
    
    weather_description = z[0]["description"]
    
    return current_temperature, weather_description
