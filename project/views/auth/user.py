from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from flask import request

api = Namespace('user')


@api.route('/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='Ok')
    def get(self):
        #header = request.headers['AUTHORIZATION']
        #token = header.split("Bearer ")[-1]
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
        return user_service.get_user_by_token(refrash_token=header)

    @api.marshal_with(user, as_list=True, code=200, description='Ok')
    def patch(self):
        req_json = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
        return user_service.update_user(data=req_json, refresh_token=header)


@api.route('/password/')
class LoginView(Resource):

    @api.marshal_with(user, as_list=True, code=200, description='Ok')
    def put(self):
        req_json = request.json
        header = request.headers.environ.get('HTTP_AUTHORIZATION').replace('Bearer ', '')
        return user_service.update_password(data=req_json, refresh_token=header)
