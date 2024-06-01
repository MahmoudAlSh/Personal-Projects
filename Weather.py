import tkinter as tk
import requests

def get_weather():
    api_key = '34c1034765d3476e553c62ff40018587'  
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city")
        return
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit_var.get()}&APPID={api_key}"
        weather_data = requests.get(url)
        weather_data.raise_for_status()  
        weather_json = weather_data.json()
        
        temperature = weather_json['main']['temp']
        humidity = weather_json['main']['humidity']
        weather_description = weather_json['weather'][0]['description']
        
        result_label.config(text=f"Temperature: {temperature} {unit_var.get()}\nHumidity: {humidity}%\nDescription: {weather_description}")
        
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"An error occurred: {e}")

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter a city:")
city_label.grid(row=0, column=0 , padx = 5 , pady = 5)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1 , padx = 5 , pady = 5)

unit_var = tk.StringVar(value="imperial")
unit_frame = tk.Frame(root)
unit_frame.grid(row=1, column=0, columnspan=2 , padx= 5 , pady= 5)

imperial_radio = tk.Radiobutton(unit_frame, text="Imperial (F)", variable=unit_var, value="imperial")
imperial_radio.pack(side="left")

metric_radio = tk.Radiobutton(unit_frame, text="Metric (C)", variable=unit_var, value="metric")
metric_radio.pack(side="left")

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.grid(row=2, column=0, columnspan = 2 , padx = 5 , pady = 5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan = 2, padx = 5 , pady= 5 )

root.mainloop()
