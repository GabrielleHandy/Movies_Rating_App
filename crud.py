"""CRUD operations"""
from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    '''Return a list of all users'''

    return User.query.all()

def get_user_by_id(user_id):
    '''Return a specific user'''

    return User.query.get(user_id)

def get_user_by_email(email):
    '''Return a user by email'''

    user = User.query.filter(User.email == email).first()
    return user



def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    '''Return a list of all movies'''

    movies = Movie.query.all()
    return movies

def get_movie_by_id(movie_id):
    
    return Movie.query.get(movie_id)

def create_rating(user, movie, score):
    """Create and return a new rating"""
    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_rating_by_user_movie(user_id, movie_id):
    return Rating.query.filter(Rating.movie_id == movie_id, Rating.user_id == user_id).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)