from .auth import auth_ns, user_ns
from .main import genres_ns
from .directors import api as directors_ns
from .movies import api as movies_ns

__all__ = [
    'auth_ns',
    'genres_ns',
    'user_ns',
    'movies_ns',
    'directors_ns'
]
