from utils import convert_currency
from utils import get_weather

from datetime import date, datetime
import copy
from colorama import init as colorama_init
from colorama import Fore, Style
from data import city, text_path

# initialize colorama for the terminal output colored text
colorama_init()
city = city
text_file = text_path

try:
    with open(text_path, 'r') as file:
        text = file.read()

        usd_rub_rate = convert_currency('USD', 'RUB', 1)
        amd_usd_rate = convert_currency('AMD', 'USD', 1000)
        amd_rub_rate = convert_currency('AMD', 'RUB', 1000)
        btc_usd_rate = convert_currency('BTC', 'USD', 1)
        eth_usd_rate = convert_currency('ETH', 'USD', 1)

        date_today = date.today().strftime("%B %d %Y")
        date_time = str(datetime.now().hour) + ':' + str(datetime.now().minute)

        weather_temperature, weather_status = get_weather(city)

        data = {
            'date_today': Fore.YELLOW + str(date_today) + Style.RESET_ALL,
            'date_time': Fore.YELLOW + str(date_time) + Style.RESET_ALL,
            'city_name': Fore.RED + city + Style.RESET_ALL,
            'weather_status': Fore.GREEN + str(weather_status) + Style.RESET_ALL,
            'weather_temperature': str(
                Fore.GREEN + str(round(weather_temperature, 2)) +'°C' + Style.RESET_ALL
                ),
            'usd_rub_rate': str(round(usd_rub_rate, 2)),
            'amd_rub_rate': str(round(amd_rub_rate, 2)),
            'amd_usd_rate': str(round(amd_usd_rate, 2)),
            'btc_usd_rate': str(round(btc_usd_rate, 2)),
            'eth_usd_rate': str(round(eth_usd_rate, 2))
            }

        formatted_text = copy.deepcopy(text)

        for key, value in data.items():
            formatted_text = formatted_text.replace(key, value)

        print(formatted_text)

except:
    print("Failed to establish a connection. Make sure you have internet!")