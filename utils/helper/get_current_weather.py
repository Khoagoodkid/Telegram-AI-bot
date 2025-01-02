import requests
import os 
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_current_weather(lat:str, long:str, unit: str):
    response = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={lat},{long}&days=2")
  
    if response.status_code == 200:
        data = response.json()
        degree =  data.get('current').get('temp_c')
        if not unit == "celsius":
            degree = data.get('current').get('temp_f')
        description = data.get('current').get('condition').get('text')
        return str(degree) + " " + str(description)
        # print(data)
    
    return f"Failed to retrieve data: {response.status_code}"
   