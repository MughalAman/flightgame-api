from flask import Blueprint, Response
import os
from mapbox import Geocoder

maps = Blueprint('maps', __name__, url_prefix='/maps')

os.environ['MAPBOX_ACCESS_TOKEN'] = "pk.eyJ1Ijoic2FudHR1amsiLCJhIjoiY2xiamc0MnE3MDU4MTN1bm80aW4wMm1sMCJ9.K4uuOEAe5iOW6wtezCzUyw"
geocoder = Geocoder(access_token=os.environ['MAPBOX_ACCESS_TOKEN'])

@maps.route('/')
def get_map():

    response = geocoder.forward("Helsinki")

    coordinates = response.geojson()['features'][0]['geometry']['coordinates']

    return f"<img src='https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/{coordinates[0]},{coordinates[1]},12.0,0,0/1200x800?access_token={os.environ['MAPBOX_ACCESS_TOKEN']}'>"

