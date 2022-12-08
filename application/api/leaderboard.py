from flask import Blueprint, Response
import json

leaderboard = Blueprint('leaderboard', __name__, url_prefix='/leaderboard')