from flask import Blueprint, Response
import json
from application.database_connector import get_countries

countries = Blueprint('countries', __name__, url_prefix='/countries')

@countries.route('/')
def get_countries():
    countries = get_countries()
    return countries