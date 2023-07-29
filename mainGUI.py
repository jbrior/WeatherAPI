import requests
import tkinter as tk
from random import randint
import main


def get_weather(city):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    try:
        querystring = {"q": city}
        headers = {
            "X-RapidAPI-Key": main.API_KEY,
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }
        data = (requests.get(url, headers=headers, params=querystring)).json()
        weather_data = {
            'city_name': data['location']['name'],
            'state': data['location']['region'],
            'temperature': data['current']['temp_f'],
            'description': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind': data['current']['wind_mph'],
        }
        return weather_data
    except Exception:
        return None

def show_weather(x=False):
    city = entry_city.get() if not x else randint(10_000,99_999)
    weather = get_weather(city)
    if weather:
        weather_info.config(text=f"{weather['city_name']}, {weather['state']}\n"
                                 f"Temperature: {weather['temperature']}°F\n"
                                 f"Description: {weather['description']}\n"
                                 f"Humidity: {weather['humidity']}%\n"
                                 f"Wind Speed: {weather['wind']} mph")
    else:
        weather_info.config(text="City not found")

# Create the GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Create Text Field
entry_city = tk.Entry(root)
entry_city.pack(pady=10)

# Create Buttons
button1 = tk.Button(root, text="Get Weather", command=show_weather)
button1.pack()
button2 = tk.Button(root, text="Get Random Weather", command=lambda: show_weather(x=True))
button2.pack()

#Create Label
weather_info = tk.Label(root, font=('Helvetica', 14))
weather_info.pack(pady=10)

root.mainloop()
