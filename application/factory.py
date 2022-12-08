from flask import Flask
from application.api.countries import countries
from application.api.countries import jobs
from application.api.countries import leaderboard
from application.api.countries import weather


def create_app():
    app = Flask(__name__)
    app.register_blueprint(countries)
    app.register_blueprint(jobs)
    app.register_blueprint(leaderboard)
    app.register_blueprint(weather)
    return app