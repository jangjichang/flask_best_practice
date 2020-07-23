from flask import jsonify, request
from flask_restx import Api
from .movies.v1.urls import url_configuration
from .setting.settings import create_app

app = create_app(__name__)
api = Api(app)

url_configuration(api)
