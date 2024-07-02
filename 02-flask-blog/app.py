from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm
from models import User, Post
# Issue: running flask blog script from a cmd causes import error - cannot import User from models
# Expelenation: importing sth from a module runs the entire module 
# 1. running application from cmd with `python app.py`` runs actually __main__ (and renames app to this), 
#    the `from models import User` statement is found - and models module is run
# 2. inside models.py there is `from app import db` - so app module is run (for the second time)
#    `from models import User` is found again, and python thinks "ok I've already seen that"
#    but since definition of User class is below the import (db) statement - it does not know it and fails on the `User` import not on the `db` import
# Solutions:
# 1.(Ugly) move abpve import below db creation - but then creating the db 
#   (cmd: from app import db; db.create_all()) would throw an error - db is not defined 
# 2. not running the app.py directly - no __main__ name created 

app = Flask(__name__)

# secret key - disables modifing cookies and cross-site request forgery attacks
app.config["SECRET_KEY"] = "a18ce0d0a5b01a64847dd7de7512e6d2"
# to build the random string of characters (in terminal):
#  import secrets
#  secrects.token_hex(16)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# /// - means the relative path from the current file
db = SQLAlchemy(app)
app.app_context().push()  # needed for running in terminal: python - from app import db - db.create_all()
    

posts = [
    {
        "author": "Corey Schafer",
        "title": "Post 1",
        "content": "First post content",
        "date_posted": "Aptil 1, 2020"
    },
    {
        "author": "Jane Dough",
        "title": "Post 2",
        "content": "Second post content",
        "date_posted": "Aptil 2, 2020"
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html",  title="About")


@app.route("/register", methods=["GET", "POST"])  # list of allowed method
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")  # succes is the bootstrap class   
        return redirect(url_for("home"))
    # this is not the best idea... since loading the empty form also triggers this
    # else:
    #     flash(f"Account not created! Errors: {form.errors}", "danger")
    # better one is shown in the register.html - search for 'is-invalid'
    return render_template("register.html", title="Register", form=form)    


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "d.trojanowsk@gmail.com" and form.password.data == "123":
            flash("You're have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form) 


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    #     print("Database created!")
    app.run(debug=True)
