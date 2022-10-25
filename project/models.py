from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from project.setup.db.db import db
from project.setup.db.models import Base


class Genre(Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=False, nullable=False)


class Director(Base):
    __tablename__ = 'directors'

    name = Column(String(250), unique=False, nullable=False)


class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=False, nullable=False)
    description = Column(String(255), unique=False, nullable=False)
    trailer = Column(String(255), unique=False, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=False)
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey('directors.id'), nullable=False)
    director = relationship("Director")


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre = Column(String(255),ForeignKey(f'{Genre.__tablename__}.id'))
    genre = relationship("Genre")

