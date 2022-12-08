from flask import Blueprint, Response
import json

weather = Blueprint('weather', __name__, url_prefix='/weather')