# weather_utils.py
# This module contains utility functions for fetching weather data from WeatherAPI.com.

import requests
from weather_module import Weather  # Import the Weather class from the module

API_KEY = '724325c629124f48bf1134529250109'  # Replace with your actual WeatherAPI.com API key
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def fetch_weather(city):
    """
    Fetches current weather data for a given city using WeatherAPI.com.
    
    Args:
        city (str): The name of the city to fetch weather for.
    
    Returns:
        Weather: A Weather object if successful, None otherwise.
    """
    params = {
        'key': API_KEY,
        'q': city
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for bad status codes (4xx/5xx)
        
        data = response.json()
        
        if 'error' in data:
            print(f"Error fetching weather for {city}: {data['error']['message']}")
            return None
        
        # Extract relevant data
        location = data['location']
        current = data['current']
        
        weather = Weather(
            city=location['name'],
            temperature=current['temp_c'],
            condition=current['condition']['text'],
            humidity=current['humidity'],
            wind_speed=current['wind_kph'],
            last_updated=current['last_updated']
        )
        return weather
    
    except requests.exceptions.RequestException as e:
        print(f"Network error fetching weather for {city}: {e}")
        return None
    except KeyError as e:
        print(f"Unexpected response format for {city}: Missing key {e}")
        return None