import base64
import hashlib
import jwt
import datetime
import calendar
from flask import current_app
from project.constants import secret, algo

def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compare_password_hash(password_hash, other_password) -> bool:
    return password_hash == generate_password_hash(other_password)


def generate_tokens(email, password, password_hash=None, is_refresh=False):
    if email is None:
        return None

    if not is_refresh:
        if not compare_password_hash(other_password=password, password_hash=password_hash):
            return None

    data = {
        "email": email,
        "password": password
    }
    # 15 minutes token
    min15 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
    data["exp"] = calendar.timegm(min15.timetuple())
    #access_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
                              #algorithm=current_app.config['ALGORITHM'])
    access_token = jwt.encode(data, secret, algorithm=algo)

    # 130 days token
    day130 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
    data["exp"] = calendar.timegm(day130.timetuple())
    #refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'],
    #                          algorithm=current_app.config['ALGORITHM'])
    refresh_token = jwt.encode(data, secret, algorithm=algo)

    tokens = {"access_token": access_token, "refresh_token": refresh_token}
    return tokens


def approve_refresh_token(refresh_token):
    data = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'],
                      algorithms=[current_app.config['ALGORITHM']])
    email = data.get("email")
    password = data.get("password")
    return generate_tokens(email, password, is_refresh=True)


def get_data_from_token(refresh_token):
    try:
        data = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'],
                      algorithms=[current_app.config['ALGORITHM']])
        return data
    except Exception as e:
        print(e)
        return None

# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)
