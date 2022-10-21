from flask_restx import fields, Model

from project.setup.api.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Иван'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Иван Васильевич'),
    'description': fields.String(required=True, max_length=300, example='Нормальный фильм'),
    'trailer': fields.String(required=True, max_length=300, example='link'),
    'year': fields.Integer(required=True, example=2022),
    'rating': fields.Float(required=True, example=1.0),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director)
})


user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'password': fields.String(required=True, max_length=100, example='123@jhgfyL'),
    'email': fields.String(required=True, max_length=100, example='123@jhjhh.ru'),
    'name': fields.String(required=True, max_length=100, example='Иван Васильевич'),
    'surname': fields.String(required=True, max_length=100, example='Васильев'),
    'genre': fields.Nested(genre)
})

