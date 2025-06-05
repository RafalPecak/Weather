import os
from excel import save_to_excel
from openweather_data import fetch_weather
from dotenv import load_dotenv
import time
load_dotenv()

api_key = os.getenv("OPENWEATHER_KEY")
api_city = os.getenv("OPENWEATHER_CITY")
excel_path = os.getenv("EXCEL_FILE_PATH")
interval = float(os.getenv("CRON_INTERVAL"))

while True:
    weather_results = fetch_weather(api_key,api_city)
    save_to_excel(weather_results, excel_path)
    print(f"Zapisano dane {weather_results['datetime']}")
    time.sleep(interval)

