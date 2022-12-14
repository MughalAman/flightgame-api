from flask import Blueprint, Response
import os
import json


leaderboard = Blueprint('leaderboard', __name__, url_prefix='/leaderboard')


@leaderboard.route('/')
def get_leaderboard():
    file_path = os.path.join(os.path.dirname(__file__), 'leaderboard.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return json.dumps(data)
