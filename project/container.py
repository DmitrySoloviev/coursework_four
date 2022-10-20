from project.dao.main import GenresDAO, DirectorsDAO, MoviesDAO, UsersDAO
from project.services import GenresService, UsersService, MoviesService, DirectorsService
from project.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorsDAO(db.session)
movie_dao = MoviesDAO(db.session)
user_dao = UsersDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=director_dao)
user_service = UsersService(dao=director_dao)