

import requests


def main():
    """Retrieve weather forecast data from OpenWeatherMap"""
    user_input = 0
    while user_input != 2:
        user_input = welcome()
        if user_input == 1:
            area = input("\nPlease enter your city name:").title()
            api_key = '8b653b1b55e1f4816a5e34e529546a98'
            # api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
            full_link = 'https://api.openweathermap.org/data/2.5/weather?q= + area' + '&units=imperial&appid=' + api_key
            try:
                api_link = requests.get(full_link)
            except ConnectionError:
                print(f"Unable to connect to {full_link}")
            else:
                print("Connection successful.")
                api_data = api_link.json()

                if api_data['cod'] == '404':
                    print("\nCity name not valid. Please try again.")
                else:
                    description = (api_data['weather'][0]['description'])
                    temperature = (api_data['main']['temp'])
                    humidity = (api_data['main']['humidity'])
                    wind_speed = (api_data['wind']['speed'])

                    print(f"Weather in {area}:")
                    print(f"Current weather description: {description.title()}")
                    print('Temp: {:.1f}F'.format(temperature))
                    print(f"Humidity: {humidity}%")
                    print(f"Wind speed: {wind_speed}mph")

        if user_input == 2:
            print("\nThank you for using Python Weather Forecast")
            break


def welcome():
    print("\nWelcome to Python Weather Forecast")
    print("\nEnter 1 to request weather for a city. Enter 2 to quit.")
    try:
        return int(input("Please choose an option from the menu:"))
    except ValueError:
        print("Input is not valid. Please try again.")


main()
