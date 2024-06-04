import requests
import sys


def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_weather(data):
    if data:
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"weather Conditions: {weather}")
    else:
        print("Error retrieving weather data. Please check the location or try again later.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python weather.py <API_KEY> <LOCATION>")
        sys.exit(1)

    api_key = sys.argv[1]
    location = sys.argv[2]

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
