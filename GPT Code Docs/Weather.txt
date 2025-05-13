# weather.py - Bee Ticker v5.1 module with config file

import requests
import json
import os

def load_api_key():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    return config["OPENWEATHER_API_KEY"]

API_KEY = load_api_key()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_current_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_data
    else:
        print(f"Error fetching weather: {response.status_code}")
        return None
