#

import requests
import os


def main():
    user_input = 0
    while user_input != 2:
        user_input = welcome()
        if user_input == 1:
            area = input("\nPlease enter your city name:").title()
            api_key = os.environ['current_weather_data']
            # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
            full_link = 'https://api.openweathermap.org/data/2.5/weather?q=' + area + '&units=imperial&appid=' + api_key
            api_link = requests.get(full_link)
            api_data = api_link.json()

            if api_data['cod'] == '404':
                print("City name not valid. Please try again.")
            else:
                description = (api_data['weather'][0]['description'])
                temperature = (api_data['main']['temp'])
                humidity = (api_data['main']['humidity'])
                wind_speed = (api_data['wind']['speed'])

                print(f"Weather in {area}:")
                print(f"Current weather description: {description.title()}")
                print('Temp: {:.1f}F'.format(temperature))
                print(f"Humidity: {humidity}%")
                print(f"Wind speed: {wind_speed}")

        if user_input == 2:
            print("\nThank you for using Python Weather Forecast")
            break


def welcome():
    print("\nWelcome to Python Weather Forecast")
    print("\nEnter 1 to request weather for a city. Enter 2 to quit.")
    return int(input("Please choose an option:"))


main()
