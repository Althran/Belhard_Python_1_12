from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Float
from db.base import Base


class Persons(Base):

    __tables__ = 'persons'

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    surname = Column(String(), nullable=False)
    birth_date = Column(DATETIME(), nullable=False)
    relations_1 = relationship('Users')
    relations_2 = relationship('Films')
    relations_3 = relationship('CharactersActors')


class UserTypes(Base):

    __tables__ = 'user_types'

    id = Column(String(), nullable=False, primary_key=True)
    name = Column(String(), nullable=False)
    relations = relationship('Users')


class Users(Base):

    __tables__ = 'users'

    login = Column(String(), nullable=False, primary_key=True)
    password = Column(String(), nullable=False)
    user_type_id = Column(String(), ForeignKey('user_type.id'), nullable=False)
    person_id = Column(Integer(), ForeignKey('persons.id'), nullable=False)
    relations = relationship('Emails')


class Emails(Base):

    __tables__ = 'emails'

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    user_login = Column(String(), ForeignKey('users.login'), nullable=False)


class Genres(Base):

    __tables__ = 'genres'

    id = Column(String(), nullable=False, primary_key=True)
    name = Column(String(), nullable=False)
    relations_1 = relationship('UserFavoriteFilms')
    relations_2 = relationship('FilmsGenres')


class Films(Base):

    __tables__ = 'films'

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    duration = Column(Integer(), nullable=False)
    name = Column(String(), nullable=False)
    release_date = Column(DATETIME(), nullable=False)
    rating = Column(Float(), nullable=False)
    director_id = Column(Integer(), ForeignKey('persons.id'), nullable=False)
    relations_1 = relationship('UserFavoriteFilms')
    relations_2 = relationship('FilmsGenres')
    relations_3 = relationship('Characters')


class UserFavoriteFilms(Base):

    __tables__ = 'user_favorite_films'

    user_login = Column(String(), ForeignKey('users.login'), nullable=False)
    film_id = Column(Integer(), ForeignKey('films.id'), nullable=False)


class FilmsGenres(Base):

    __tables__ = 'films_genres'

    film_id = Column(Integer(), ForeignKey('films.id'), nullable=False)
    film_genre_id = Column(String(), ForeignKey('genres.id'), nullable=False)


class Characters(Base):

    __tables__ = 'characters'

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    comment = Column(String())
    film_id = Column(Integer(), ForeignKey('films.id'), nullable=False)
    relations_1 = relationship('CharactersActors')


class CharactersActors(Base):

    __tables__ = 'characters_actors'

    character_id = Column(Integer(), ForeignKey('characters.id'), nullable=False)
    person_id = Column(Integer(), ForeignKey('persons.id'), nullable=False)
