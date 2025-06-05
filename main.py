import os
from excel import save_to_excel
from openweather_data import fetch_weather
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENWEATHER_KEY")
api_city = os.getenv("OPENWEATHER_CITY")

weather_results = fetch_weather(api_key,api_city)
save_to_excel(weather_results)
