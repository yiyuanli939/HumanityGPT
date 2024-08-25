import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import pymysql

# Use pymysql to connect to the MySQL database
pymysql.install_as_MySQLdb()

# Initialize SQLAlchemy
db = SQLAlchemy()


def create_app():
    # Initialize the Flask app with necessary configurations & extensions
    app = Flask(__name__)
    Bootstrap5(app)

    # Configure the MySQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://humanitygpt_user:67ti8of87690hm@localhost/humanitygpt'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Set template and static folders
    # These are mainly HTML files that are rendered by the backend
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'frontend', 'templates'))
    app.template_folder = template_dir
    # These are mainly CSS, JavaScript, and image files that are served by the backend
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'frontend', 'static'))
    app.static_folder = static_dir


    print(f"Template folder set to: {app.template_folder}")
    print(f"Static folder set to: {app.static_folder}")

    # Initialize the app with the database
    from .models import User
    db.init_app(app)

    # Create the database tables
    with app.app_context():
        db.create_all()



    # Define routes (you can move these to a separate file later if desired)
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html',name = name)
    
    @app.route('/test')
    def test():
        return render_template('test.html')
    # Test whether the database connection is successful
    @app.route('/test_db')
    def test_db():
        try:
            db.session.query(User).first()
            return "Database connection successful!"
        except Exception as e:
            return f"Database connection failed: {str(e)}"

    # Return the configured app instance
    return app