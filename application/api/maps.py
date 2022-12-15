from flask import Blueprint, Response, request



maps = Blueprint('maps', __name__, url_prefix='/maps')

maps_token = "pk.eyJ1Ijoic2FudHR1amsiLCJhIjoiY2xiamc0MnE3MDU4MTN1bm80aW4wMm1sMCJ9.K4uuOEAe5iOW6wtezCzUyw"

@maps.route('/')
def get_map():
    args = request.args
    start_lat = float(args.get("start1"))
    start_lng = float(args.get("start2"))
    end_lat1 = float(args.get("end1_1"))
    end_lng1 = float(args.get("end1_2"))
    end_lat2 = float(args.get("end2_1"))
    end_lng2 = float(args.get("end2_2"))
    end_lat3 = float(args.get("end3_1"))
    end_lng3 = float(args.get("end3_2"))

    api_map = f"<img src='https://api.mapbox.com/styles/v1/mapbox/dark-v11/static/pin-s+ff0000({start_lat},{start_lng}),pin-s+8f00ff({end_lat1},{end_lng1}),pin-s+8f00ff({end_lat2},{end_lng2}),pin-s+8f00ff({end_lat3},{end_lng3})/20,57,3.1,0,0/1200x800?access_token={maps_token}'>"


    return api_map
