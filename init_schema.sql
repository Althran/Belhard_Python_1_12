DROP DATABASE IF EXISTS film_zone;
CREATE DATABASE film_zone;
USE film_zone;
CREATE TABLE persons (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    birth_date DATETIME NOT NULL
);

CREATE TABLE user_types (
    id VARCHAR(50) NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

INSERT INTO user_types(id, name) VALUES ('USER', 'User');
INSERT INTO user_types(id, name) VALUES ('ADMIN', 'Administrator');

CREATE TABLE users (
    login VARCHAR(50) NOT NULL PRIMARY KEY,
    password VARCHAR(50) NOT NULL,
    user_type_id VARCHAR(50) NOT NULL,
    person_id INT NOT NULL,
    CONSTRAINT fk_users_user_types FOREIGN KEY (user_type_id)
        REFERENCES user_types (id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_users_persons FOREIGN KEY (person_id)
        REFERENCES persons (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE email (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(50) NOT NULL,
    user_login VARCHAR(50) NOT NULL,
    CONSTRAINT fk_email_users FOREIGN KEY (user_login)
        REFERENCES users (login)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE genres (
    id VARCHAR(50) NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

INSERT INTO genres(id, name) VALUES ('ACTION', 'Action');
INSERT INTO genres(id, name) VALUES ('ADVENTURE', 'Adventure');
INSERT INTO genres(id, name) VALUES ('COMEDY', 'Comedy');
INSERT INTO genres(id, name) VALUES ('DRAMA', 'Drama');
INSERT INTO genres(id, name) VALUES ('CRIME', 'Crime');
INSERT INTO genres(id, name) VALUES ('SCI_FI', 'sci-fi');
INSERT INTO genres(id, name) VALUES ('FANTASY', 'Fantasy');
INSERT INTO genres(id, name) VALUES ('MUSICAL', 'Musical');
INSERT INTO genres(id, name) VALUES ('WESTERN', 'Western');
INSERT INTO genres(id, name) VALUES ('POST_APOCALYPTIC', 'Post-apocalyptic');
INSERT INTO genres(id, name) VALUES ('WAR', 'War');
INSERT INTO genres(id, name) VALUES ('FAMILY', 'Family_film');
INSERT INTO genres(id, name) VALUES ('LOVE', 'Love_story');
INSERT INTO genres(id, name) VALUES ('CARTOON', 'Cartoon');
INSERT INTO genres(id, name) VALUES ('HORROR', 'Horror');
INSERT INTO genres(id, name) VALUES ('THRILLER', 'Thriller');
INSERT INTO genres(id, name) VALUES ('DOCUMENTARY', 'Documentary');

CREATE TABLE films (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    duration INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    realese_date DATETIME NOT NULL,
    rating FLOAT NOT NULL,
    director_id INT NOT NULL,
    CONSTRAINT fk_films_presons FOREIGN KEY (director_id)
        REFERENCES persons (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE user_favorite_films (
    user_login VARCHAR(50) NOT NULL,
    film_id INT NOT NULL,
    CONSTRAINT fk_user_favorite_films_users FOREIGN KEY (user_login)
        REFERENCES users (login)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_user_favorite_films_films FOREIGN KEY (film_id)
        REFERENCES films (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE films_genres (
    film_id INT NOT NULL,
    film_genre_id VARCHAR(50) NOT NULL,
    CONSTRAINT fk_film_genres_films FOREIGN KEY (film_id)
        REFERENCES films (id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_film_genres_genres FOREIGN KEY (film_genre_id)
        REFERENCES genres (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE characters (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    comment VARCHAR(50),
    film_id INT NOT NULL,
    CONSTRAINT fk_characters_films FOREIGN KEY (film_id)
        REFERENCES films (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE characters_actors (
    character_id INT NOT NULL,
    person_id INT NOT NULL,
    CONSTRAINT fk_characters_actors_characters FOREIGN KEY (character_id)
        REFERENCES characters (id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_characters_actors_persons FOREIGN KEY (person_id)
        REFERENCES persons (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
 