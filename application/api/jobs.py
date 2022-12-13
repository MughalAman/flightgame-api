from flask import Blueprint, Response
import json

jobs = Blueprint('jobs', __name__, url_prefix='/jobs')

