from sqlalchemy.orm.scoping import scoped_session

from project.dao.base import BaseDAO
from project.models import Genre, Director, Movie, User
from project.tools.security import generate_password_hash
from typing import Optional
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql.expression import desc
from werkzeug.exceptions import NotFound


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_buy(self, filter: Optional[str], page: int):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        if filter:
            stmt = stmt.order_by(desc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def __init__(self, db_session: scoped_session):
        super().__init__(db_session)
        self.db = None

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
            #db.session.rollback()

    def get_user_by_login(self, email):
        try:
            #stmt = db.session.query(self.__model__).filter(self.__model__.email == email).all[0]
            stmt = self._db_session.query(self.__model__).filter(self.__model__.email == email).one()
            #stmt = db.session.query(User).filter(User["email"] == email).one()
            return stmt
        except Exception as e:
            print(e)
            return {}

    def update(self, email, data):
        try:
            #db.session.query(self.__model__).filter(self.__model__.email == email).update(data)
            self._db_session.query(self.__model__).filter(self.__model__.email == email).update(data)
            self._db_session.commit()
        except Exception as e:
            print(e)
            self._db_session.rollback()
            #db.session.rollback()



