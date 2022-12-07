from flask import Flask
from application.api.countries import countries


def create_app():
    app = Flask(__name__)
    app.register_blueprint(countries)

    return app