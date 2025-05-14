# weather.py - Bee Ticker v5.4.1 polished weather module

import requests
import json
import os
from typing import Optional, Dict

def load_api_key() -> str:
    """Load the OpenWeatherMap API key from config.json."""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config["OPENWEATHER_API_KEY"]
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        raise ValueError("Missing or invalid API key in config.json.")

API_KEY = load_api_key()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_current_weather(city: str) -> Optional[Dict[str, str]]:
    """
    Fetch current weather data for the given city.

    Returns a dictionary with weather info or None if request fails.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]
        }
        return weather_data
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching weather: {e}")
        return None
