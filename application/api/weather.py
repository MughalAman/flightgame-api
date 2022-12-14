from flask import Blueprint, Response, request
import requests
import json

weather = Blueprint('weather', __name__, url_prefix='/weather')



@weather.route('/')
def get_weather():
    args = request.args
    lat = float(args.get("lat"))
    lon = float(args.get("lon"))
    answer = weather_api_call(lat, lon)
    result = turn_into_json(answer)
    return result

def turn_into_json(sql_list):
    sql_print = {
        "temperature": sql_list["main"]["temp"],
        "windspeed": sql_list["wind"]["speed"]
    }
    result = json.dumps(sql_print)
    return result

def weather_api_call(lat, lon):
    API_key = "536025f917f606d3f38261ae0276b78c"

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
    try:
        weather_info = requests.get(weather_url)
        if weather_info.status_code == 200:
            final = weather_info.json()

    except requests.exceptions.RequestException as e:
        print("virhe")

    return final