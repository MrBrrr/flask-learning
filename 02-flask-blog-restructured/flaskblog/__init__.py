from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config["SECRET_KEY"] = "a18ce0d0a5b01a64847dd7de7512e6d2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
app.app_context().push()  # needed for running in terminal: python - from app import db - db.create_all()
db.session.add
bcrypt  = Bcrypt(app)
# bcrypt hashes the password

login_manager = LoginManager(app)
# login_manager handles users' session management in the background 

login_manager.login_view = "login"  # the same thing that is passed to the url_for function
# if the route with `@login_required` failed, the user is redirected to the 
# `login` page with message: Please log in to access this page.
login_manager.login_message_category = "info"  # bootstrap class for the message

from flaskblog import routes
