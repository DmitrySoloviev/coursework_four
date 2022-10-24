
from flask_restx import Namespace, Resource
from flask import request
from project.container import user_service
from project.setup.api.models import user


api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='Ok')
    def post(self):
        req_json = request.json
        if req_json.get("email") and req_json.get("password"):
            return user_service.create(req_json.get("email"), req_json.get("password")), 201
        else:
            return "Нет данных", 401


@api.route('/login/')
class LoginView(Resource):
    @api.response(404, "Not found")
    def post(self):
        req_json = request.json
        if req_json.get("email") and req_json.get("password"):
            return user_service.check(email=req_json.get("email"), password=req_json.get("password")), 201
        else:
            return "Нет данных", 401

    @api.response(404, "Not found")
    def put(self):
        req_json = request.json
        if req_json.get("refresh_token"):
            return user_service.update_token(req_json.get("refresh_token")), 201
        else:
            return "Нет данных", 401

