from flask import Flask, render_template, redirect, url_for, request, session, flash 

from forms import RegistrationForm, LoginForm

from data_helper import get_user, insert_user
from search_engine import get_latest_movies, get_categories, get_search_movie

import ast

app = Flask(__name__)

app.secret_key = "this9is9my9secret9key"

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():

    error = None 

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        result = get_user(email=email, password=password)

        if result == 1:

            flash("Your are Login Successfully!")

            return redirect(url_for('dashbaord'))
        
        else:

            error = "Your password and username doesn't match ! Try Again"

    return render_template("login.html", error=error, form=form)

@app.route("/register", methods=["GET","POST"])
def register():

    form = RegistrationForm()

    error = None

    if form.validate_on_submit():

        username = form.name.data
        password = form.password.data
        email = form.email.data

        # hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

        print(username, password, email)

        result = insert_user(username=username, password=password, email=email)

        if result == 1:

            flash("Your are successfully registered !")

            return redirect(url_for('login'))

        else:

            error = "Email already exist!"

    return render_template("register.html", error=error, form= form)

@app.route("/dashboard", methods=["GET","POST"])
def dashbaord():

    word = request.form.get('search_word', default=None)

    print(word, "recieved")

    if word == None:

        movies = get_latest_movies()[1:]
    
    else: 
        
        movies = get_search_movie(word)
    
    return render_template("dashboard.html", movies=movies)

@app.route('/movie_detail/<movie>', methods=["GET","POST"])
def movie_detail(movie):

    movie = ast.literal_eval(movie)

    return render_template("movie_detail.html", movie=movie)


    