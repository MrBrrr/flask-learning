## Start command line

```
flask --app run.py shell
```

## database creation

```
from flaskblog import db
db.create_all()
```

## flask-bcrypt plugin

### hashing password 

```cmd
conda install flask-bcrypt
```

### generate_password_hash
```python
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
hashed_pwd = bcrypt.generate_password_hash("testing")
b'$2b$12$kaPH8WeM0blpe4VtF2Cs7eKKGJWSNDNlD1r8Vsj459zZLKSOMkK/W'  
```
Everytime the hash generated is different, even with the same password. 
Good - no breaking into account, but how to check if it's correct?

### check_password_hash
```
bcrypt.check_password_hash(hashed_pwd, "testing")  # True
bcrypt.check_password_hash(hashed_pwd, "testingqeqe")  # False
```

## flask-login plugin

This plugin handles the user session. Methods and properties provided by this plugin are available to jinja without explicit passing the as aruments to the `render_template` calls.
__init__.py
``` python
from flask_login import LoginManager
login_manager = LoginManager(app)
```

models.py
```python
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    ...
```

### UserMixin
Provides:
- is_active
- is_authenticated
- is_anonymous
- get_id


### login_user

forms.py
```python
from flask_login import login_user

@app.route("/login")
def login(self):
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            ...
        ...
    ...
```

### login_required


