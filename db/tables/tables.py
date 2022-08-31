from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Float
from db.base import Base


class Persons(Base):

    __tablename__ = 'persons'

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    surname = Column(String(), nullable=False)
    birth_date = Column(DATETIME(), nullable=False)
    relations_1 = relationship('Users')
    relations_2 = relationship('Films')
    relations_3 = relationship('CharactersActors')


class UserTypes(Base):

    __tablename__ = 'user_types'

    id = Column(String(), nullable=False, primary_key=True)
    name = Column(String(), nullable=False)
    relations = relationship('Users')


class Users(Base):

    __tablename__ = 'users'

    login = Column(String(), nullable=False, primary_key=True)
    password = Column(String(), nullable=False)
    user_type_id = Column(String(), ForeignKey('user_type.id'), nullable=False)
    person_id = Column(Integer(), ForeignKey('persons.id'), nullable=False)
    relations_1 = relationship('Emails')
    relations_2 = relationship('UserFavoriteFilms')


class Emails(Base):

    __tablename__ = 'emails'

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    user_login = Column(String(), ForeignKey('users.login'), nullable=False)


class Genres(Base):

    __tablename__ = 'genres'

    id = Column(String(), nullable=False, primary_key=True)
    name = Column(String(), nullable=False)
    relations_1 = relationship('UserFavoriteFilms')
    relations_2 = relationship('FilmsGenres')


class Films(Base):

    __tablename__ = 'films'

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

    __tablename__ = 'user_favorite_films'

    user_login = Column(String(), ForeignKey('users.login'), nullable=False, primary_key=True)
    film_id = Column(Integer(), ForeignKey('films.id'), nullable=False, primary_key=True)


class FilmsGenres(Base):

    __tablename__ = 'films_genres'

    film_id = Column(Integer(), ForeignKey('films.id'), nullable=False, primary_key=True)
    film_genre_id = Column(String(), ForeignKey('genres.id'), nullable=False, primary_key=True)


class Characters(Base):

    __tablename__ = 'characters'

    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    comment = Column(String())
    film_id = Column(Integer(), ForeignKey('films.id'), nullable=False)
    relations_1 = relationship('CharactersActors')


class CharactersActors(Base):

    __tablename__ = 'characters_actors'

    character_id = Column(Integer(), ForeignKey('characters.id'), nullable=False, primary_key=True)
    person_id = Column(Integer(), ForeignKey('persons.id'), nullable=False, primary_key=True)
