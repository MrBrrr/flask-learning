from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user

from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app
from flaskblog import db, bcrypt

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
    # get rid of register and login pages when the user is logged in
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        # don't want to pass the plain password to the database, so the hashed one is passed
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}! You can log in", "success") 
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)    


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if form.email.data == "d.trojanowsk@gmail.com" and form.password.data == "123":
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # user.passowrd - hashed one
            login_user(user, remember=form.remember.data)  # keep logged in if remember me box was checked
            flash("You're succefully logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form) 

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
