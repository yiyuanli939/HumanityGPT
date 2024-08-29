from . import db # Import the database object from the init file in models
# Define the User model

class User(db.Model):
    # the id means that this is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # the username is a string that must be unique and not null
    username = db.Column(db.String(80), unique=True, nullable=False)
    # the email is a string that must be unique and not null
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Add the relationship to documents
    documents = db.relationship('Document', backref='author', lazy='dynamic')


    # This is the constructor of the class, with the username and email as parameters
    def __init__(self, username, email):
        self.username = username
        self.email = email
    # This is a string representation of the class. 
    def __repr__(self):
        return f'<User {self.username}>'
    
    # These are the functions required by Flask-Login
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
