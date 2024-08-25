import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


def create_app():
    # Create the Flask application instance
    app = Flask(__name__)
    Bootstrap5(app)


    # Set the template folder to the frontend directory
    # These are mainly HTML files that are rendered by the backend
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'frontend', 'templates'))
    app.template_folder = template_dir

    # Set the static folder
    # These are mainly CSS, JavaScript, and image files that are served by the backend
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'frontend', 'static'))
    app.static_folder = static_dir

    print(f"Template folder set to: {app.template_folder}")
    print(f"Static folder set to: {app.static_folder}")

    # Define the main route
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html',name = name)
    
    # Define a test route
    @app.route('/test')
    def test():
        return render_template('test.html')

    # Return the configured app instance
    return app