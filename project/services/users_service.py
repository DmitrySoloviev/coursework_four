from project.dao.main import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User
from typing import Optional

from project.tools.security import generate_tokens, approve_refresh_token, get_data_from_token
from project.tools.security import generate_password_hash


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)

    def create(self, email, password):
        return self.dao.create(email, password)

    def get_user_by_login(self, email):
        return self.dao.get_user_by_login(email)

    def check(self, email, password):
        user = self.get_user_by_login(email)
        return generate_tokens(email=email, password=password, password_hash=user.password)

    def update_token(self, refresh_token):
        return approve_refresh_token(refresh_token)

    def get_user_by_token(self, refresh_token):
        data = get_data_from_token(refresh_token)
        if data:
            return self.get_user_by_login(data.get('email'))

    def update_user(self, data: dict, refresh_token):
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update(email=user.email, data=data)
            return self.get_user_by_token(refresh_token)

    def update_password(self, data: dict, refresh_token):
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update(email=user.email,
                            data={"password": generate_password_hash(data.get('password_2'))})
            return self.check(login=user.email, password=data.get('password_2'))
