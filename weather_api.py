#!/usr/bin/env python3
import requests
import json

API_KEY = "your api key here"
BASE_URL = "your base api url here"

city = "Tokyo"

params = {
    "key": API_KEY,
    "q": city,
    "aqi": "no",
}

response = requests.get(BASE_URL, params=params)

data = response.json()

icon = "?"

if response.status_code == 200 and "error" not in data:
    condition = data["current"]["condition"]["text"].lower()
    temp = data["current"]["temp_c"]
    country = data["location"]["country"]
    city = data["location"]["name"]
    humidity = data["current"]["humidity"]
    wind = data["current"]["wind_kph"]
    wind_dir = data["current"]["wind_dir"]

    if "sun" in condition or "clear" in condition:
        icon = "☀️"
    elif "partly" in condition:
        icon = "🌤️"
    elif "overcast" in condition:
        icon = "🌥️"
    elif "cloudy" in condition:
        icon = "☁️"
    elif "drizzle" in condition:
        icon = "🌦️"
    elif "rain" in condition:
        icon = "🌧️"
    elif "snow" in condition:
        icon = "❄️"
    elif "thunder" in condition:
        icon = "⚡"

    output = {"text": f" {icon}\n{temp}°C",
            "tooltip": (
                f"📍 {city}, {country}\n"
                f"{icon} {condition.title()}\n"
                f"💧 Humidity: {humidity}%\n"
                f"🌬️ Wind: {wind}k/h {wind_dir}"
                )}
else:
    output = {"icon": "?", "temp": "?", "tooltip": "Weather Data Unavailable"}

print(json.dumps(output, ensure_ascii=False), flush=True)
