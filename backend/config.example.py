import os

class Config:
    # This is a secret key used for securing sessions and other cryptographic functions
    SECRET_KEY = os.environ.get('SECRET_KEY') or "your_secret_key"
    # This is the path to the database file
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://your_user:your_password@localhost/humanitygpt'
    # This disables a feature of SQLAlchemy we don't need, which can cause extra overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False