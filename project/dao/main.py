from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User
from project.setup.db.db import db
from project.tools.security import generate_password_hash


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create(self, email, password):
        try:
            self._db_session.add(User(
                email=email,
                password=generate_password_hash(password)
            ))
            self._db_session.commit()
            print("Пользователь добавлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()

    def get_user_by_login(self, email):
        try:
            stmt = self._db_.session.query(self.__model__).filter(self.__model__.email == email).all[0]
            #stmt = db.session.query(User).filter(User["email"] == email).one()
            return stmt
        except Exception as e:
            print(e)
            return {}

    def update(self, email, data):
        try:
            self._db_.session.query(self.__model__).filter(self.__model__.email == email).update(data)
            db.session.commit()
        except Exception as e:
            print(e)
            self._db_session.rollback()



