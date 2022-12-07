from flask import Blueprint, Response
import json

countries = Blueprint('countries', __name__, url_prefix='/countries')

@countries.route('/')
def get_countries():
    pass