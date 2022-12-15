from flask import Blueprint, Response, request

maps = Blueprint('maps', __name__, url_prefix='/maps/')

maps_token = "pk.eyJ1Ijoic2FudHR1amsiLCJhIjoiY2xiamc0MnE3MDU4MTN1bm80aW4wMm1sMCJ9.K4uuOEAe5iOW6wtezCzUyw"

@maps.route('/')
def get_map():
    start_lat = float(request.args.get("start_lat"))
    start_lng = float(request.args.get("start_lng"))
    #esim http://127.0.0.1:5000/maps/?start_lat=-0.136&start_lng=51.5
    api_map = f"<img src='https://api.mapbox.com/styles/v1/mapbox/dark-v11/static/pin-s+8f00ff({start_lat},{start_lng})/20,57,3.1,0,0/1200x800?access_token={maps_token}'>"

    return api_map
