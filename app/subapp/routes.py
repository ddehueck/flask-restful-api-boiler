from app import api
from config import Config
from flask import request
from flask_restful import Resource


class ExampleView(Resource):

    def get(self):

        return {
            'field': 'This would be an example',
        }, 200

    def post(self):
        print(request)
        req_body = request.get_data()
        
        return {
            'req_body': str(req_body),
        }

api.add_resource(ExampleView, '/')
