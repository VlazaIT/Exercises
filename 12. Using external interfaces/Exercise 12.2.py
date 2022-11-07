# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api.
# Your task is to write a program that asks the user for the name of a municipality
# and then prints out the corresponding weather condition description text and temperature in Celsius degrees.
# Take a good look at the API documentation.
# Furthermore, find out how you can convert Kelvin degrees into Celsius.

import requests

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    temperature = round(response['main']['temp'] - 273.15, 1)
    weather_description = response['weather'][0]['description']
    print(f"Current temperature in {city_name} is {temperature}°C, while weather condition is {weather_description}")

city_name = input("Please, enter the municipality in the form of(City,Country Code): ")
api_key = "227f58f17cd9cd3cc5e581bd1acda34c"
get_weather(api_key, city_name)