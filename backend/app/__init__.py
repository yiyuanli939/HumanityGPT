from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from config import Config

# Create SQLAlchemy and Migrate instances without initializing them yet
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)
    
    # Load the configuration from the Config class
    app.config.from_object(Config)

    # Initialize SQLAlchemy with this app
    db.init_app(app)
    
    # Initialize Flask-Migrate with this app and db
    migrate.init_app(app, db)

    # Import the routes module
    from .routes import auth, projects, notes, pdfs
    # Register the blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(notes.bp)
    app.register_blueprint(pdfs.bp)

    # Define a simple route
    @app.route('/')
    def hello():
        return "Welcome to HumanityGPT!"

    # Return the configured app instance
    return app