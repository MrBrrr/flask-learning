from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_login import current_user

from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", 
        validators=[DataRequired(), Length(min=2, max=20)]
        )
    email = StringField(
        "Email", 
        validators=[DataRequired(), Email()]
        )
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm password", 
        validators=[DataRequired(), EqualTo("password")]   # password is a member above, but has to be string
        )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username already exsits, please choose different one.")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email already exsits, please provide different one.")
        

class LoginForm(FlaskForm):
    email = StringField(
        "Email", 
        validators=[DataRequired(), Email()]
        )
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username", 
        validators=[DataRequired(), Length(min=2, max=20)]
        )
    email = StringField(
        "Email", 
        validators=[DataRequired(), Email()]
        )
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username already exsits, please choose different one.")
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email already exsits, please provide different one.")