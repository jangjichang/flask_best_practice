from flask import Response, request
from flask_restx import Resource
import json

class MoviesAPI(Resource):
    def get(self):
        response = {"data": "movies"}
        return Response(response=json.dumps(response), status=200, mimetype="application/json")

    def post(self):
        response = {"message": "created"}
        return Response(response=json.dumps(response), status=201, mimetype="application/json")

class MovieAPI(Resource):
    def put(self, id):
        body = request.get_json()
        response = {"message": "put "+ str(id)}
        return Response(response=json.dumps(response), status=200, mimetype="application/json")
    
    def delete(self, id):
        response = {"message": "deleted " + str(id)}
        return Response(response=json.dumps(response), status=200, mimetype="application/json")

    
    def get(self, id):
        data = "movie number " +str(id)
        response = {"data": data}
        return Response(response=json.dumps(response), status=200, mimetype="application/json")
