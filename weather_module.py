# weather_module.py
# This module defines the Weather class for storing weather information.

class Weather:
    """
    A class to represent weather information for a city.
    
    """
    
    def __init__(self, city, temperature, condition, humidity, wind_speed, last_updated):
        """
        Initializes a Weather object with the provided attributes.
        
        Args:
            city (str): The name of the city.
            temperature (float): The current temperature in Celsius.
            condition (str): The current weather condition.
            humidity (int): The current humidity percentage.
            wind_speed (float): The current wind speed in km/h.
            last_updated (str): The last updated timestamp.
        """
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.last_updated = last_updated
    
    def __str__(self):
        """
        Returns a formatted string representation of the weather information.
        
        Returns:
            str: Formatted weather report for the city.
        """
        return (f"{self.city}: Temp = {self.temperature}°C, Condition = {self.condition}, "
                f"Humidity = {self.humidity}%, Wind = {self.wind_speed} km/h, "
                f"Last Updated = {self.last_updated}")