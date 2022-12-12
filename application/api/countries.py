from flask import Blueprint, Response, request
import json
from random import randint
from application.database_connector import get_countries


countries = Blueprint('countries', __name__, url_prefix='/countries')

@countries.route('/')
def get_countries_data():
    list_of_countries = get_countries()
    sql_return = get_random_airport(list_of_countries)
    result = turn_into_json(sql_return)
    return result

def get_random_airport(list_of_airports):
    # 116 viimeinen lista lentokenttä
    airport_num = randint(0, 116)
    final_airport = list_of_airports[airport_num]
    return final_airport

def turn_into_json(sql_list):
    sql_print = {
        "airport_name": sql_list[0],
        "airport_ident": sql_list[2],
        "country_name": sql_list[1],
        "country_code": sql_list[3],
        "coordinates": {
            "lat": sql_list[4],
            "lon": sql_list[5]
        },
        "price": 100
    }
    result = json.dumps(sql_print)
    return result
