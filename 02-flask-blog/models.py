from datetime import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # unique since primary key True
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpeg")  # nullable=False - default image required
    pasword = db.Column(db.String(60), nullable=False)  # hashing algorythm is 60 chars long
    # one user can have multiple posts, bu post have only one author
    posts = db.relationship("Post", backref="author", lazy=True)
    # "Post" - (uppercase) referencing actual Post class
    # backref="author" - Post will reference to the user who created the post by author field
    # lazy=True - sqlAlchemy will load the data in one go

    def __repr__(self) -> str:  # how the object is printed
        return f"User {self.username}, {self.email}, {self.image_file}"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    content = db.Column(db.Text, nullable=False)
    # db.ForeignKey("user.id") - relationship with the User table
    # "user.id" - user (lowercase) represents actual table name and id is the column name
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self) -> str:
        return f"User {self.title}, {self.date_posted}, {self.content}"
