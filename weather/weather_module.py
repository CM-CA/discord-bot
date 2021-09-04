# Create class for weather module


# Imports
import requests
import json
import datetime
import time
import os
import sys
from dotenv import load_dotenv


# Class
class WeatherModule:
    """
    Weather module class
    """

    # Initialize
    def __init__(self, city):
        """
        Initialize WeatherModule class
        """
        # Create instance of class
        self.city = city

    # Method
    def get_weather(self):
        """
        Get weather data
        """
        # Set up request
        load_dotenv()
        url = (
            "http://api.openweathermap.org/data/2.5/weather?q="
            + self.city
            + "&units=metric"
            + "&lang=sp"
            + "&APPID="
            + os.getenv("OPENWEATHERMAP_API_KEY")
        )
        # Get data
        data = requests.get(url).json()
        # Return data
        description = data.get("weather")[0].get("description")
        temp = data.get("main").get("temp_max")
        return description

    def get_temperature(self):
        load_dotenv()
        url = (
            "http://api.openweathermap.org/data/2.5/weather?q="
            + self.city
            + "&units=metric"
            + "&lang=sp"
            + "&APPID="
            + os.getenv("OPENWEATHERMAP_API_KEY")
        )
        # Get data
        data = requests.get(url).json()
        # Return data
        temp = data.get("main").get("temp_max")
        return temp
