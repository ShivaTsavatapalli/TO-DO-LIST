import requests

def get_weather_data(location):
    api_key = "YOUR_API_KEY_HERE"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == "404":
        print("City not found. Please check the city name or zip code.")
        return

    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    print(f"Weather for {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description}")

def main():
    location = input("Enter city name or zip code: ")
    weather_data = get_weather_data(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
