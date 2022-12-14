from flask import Flask
from application.api.countries import countries
from application.api.jobs import jobs
from application.api.leaderboard import leaderboard
from application.api.weather import weather
from application.api.maps import maps

from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    app.register_blueprint(countries)
    app.register_blueprint(maps)
    app.register_blueprint(jobs)
    app.register_blueprint(leaderboard)
    app.register_blueprint(weather)

    return app