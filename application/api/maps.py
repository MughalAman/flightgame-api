from flask import Blueprint, Response, request
import json


maps = Blueprint('maps', __name__, url_prefix='/maps/')

maps_token = "pk.eyJ1Ijoic2FudHR1amsiLCJhIjoiY2xiamc0MnE3MDU4MTN1bm80aW4wMm1sMCJ9.K4uuOEAe5iOW6wtezCzUyw"

@maps.route('/')
def get_map():
    start_lat = float(request.args.get("start_lat"))
    start_lon = float(request.args.get("start_lon"))
    #esim http://127.0.0.1:5000/maps/?start_lat=-0.136&start_lon=51.5
    api_map_source = f"https://api.mapbox.com/styles/v1/mapbox/dark-v11/static/pin-s+8f00ff({start_lat},{start_lon})/{start_lat},{start_lon},3.1,0,0/1200x800?access_token={maps_token}"\
    
    respone_dict = {"map_source": api_map_source}

    return Response(json.dumps(respone_dict), mimetype='application/json', status=200)
