# weather.py - Bee Ticker v5.1 module

import requests

API_KEY = "ac6379682e40ee7caec07c8112871aee"  
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
