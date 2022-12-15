from flask import Blueprint, Response, request
import json
from random import randint
from application.database_connector import get_countries
from geopy.distance import geodesic as distance_km


countries = Blueprint('countries', __name__, url_prefix='/countries')

@countries.route('/')
def get_countries_data():
    list_of_countries = get_countries()
    airports = []
    while len(airports) < 3:
        sql_list = get_random_airport(list_of_countries)
        airport = \
        {"airport_name": sql_list[0],
        "airport_ident": sql_list[2],
        "country_name": sql_list[1],
        "country_code": sql_list[3],
        "coordinates": {
            "lat": sql_list[4],
            "lon": sql_list[5]
        },
        "price": 100
    }
        if airport not in airports:
            airports.append(airport)
    return Response(json.dumps(airports), mimetype='text/html', status=200)

def get_random_airport(list_of_airports):
    # 116 viimeinen lista lentokenttä
    airport_num = randint(0, 116)
    final_airport = list_of_airports[airport_num]
    return final_airport


def count_distance(start, end):
    return round(distance_km(start, end).km, 2)

def count_co2_consumed(distance):
    return round((distance*0.176), 0)


#http://127.0.0.1:5000/countries/flight_info?start_lat=10.10&start_lon=10.10&end_lat=20.20&end_lon=20.20
@countries.route('/flight_info')
def flight_info():
    start_airport_lat = float(request.args.get("start_lat"))
    start_airport_lon = float(request.args.get("start_lon"))
    end_airport_lat = float(request.args.get("end_lat"))
    end_airport_lon = float(request.args.get("end_lon"))
    start_airport = (start_airport_lat, start_airport_lon)
    end_airport = (end_airport_lat, end_airport_lon)
    distance = count_distance(start_airport, end_airport)
    result = count_co2_consumed(distance)
    counted_info = {
                    "distance": distance,
                    "co2_consumed": result
                    }

    return Response(json.dumps(counted_info), mimetype='text/html', status=200)
