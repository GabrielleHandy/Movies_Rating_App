"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'VincenzoGoblin'
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def hompage():
    """View Hompage"""
    # add check if in session
    return render_template('homepage.html')
    

@app.route('/movies')
def list_movies():
    """View List of all movies"""
    
    movies = crud.get_movies()
    return render_template('all_movies.html', movies= movies)
    

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    '''Show details of specific movie'''
    movie = crud.get_movie_by_id(movie_id)
    rating = crud.get_rating_by_user_movie(session['user_id'], movie_id)
    return render_template('movie_details.html', movie=movie, rating = rating)
    

@app.route('/users')
def list__users():
    """View a list of all users"""
    users = crud.get_users()
    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def create_account():
    """Create an account"""
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    if user:
        flash('Email already in use. :(')
         
    else:
        crud.create_user(email, password)
        flash('Account created! :)')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login_user():
    '''Log in user'''
    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    if user:
        if user.password == password:
            flash("Logged in :)")
            session['user_id'] = user.user_id
            print(session)
        else:
            flash("Incorrect password :(")
    else:
        flash("Email does not exist :(")

    return redirect('/')


@app.route('/users/<user_id>')
def show_user(user_id):
    '''Show user info'''
    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)

@app.route('/rating/<movie_id>', methods=['POST'])
def add_rating(movie_id):
    rating = request.form.get('rating')

    movie = crud.get_movie_by_id(movie_id)
    user = crud.get_user_by_id(session.get('user_id'))

    crud.create_rating(user, movie, int(rating))

    return redirect('/')


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
