import os
from flask import Flask, render_template, redirect, url_for, flash
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
    # Add a secret key for CSRF protection
    app.config['SECRET_KEY'] = '2b62b1cb0b257df9d873558f82151351e15c6ff268b20941'  

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
    
    # Add a new route for user pages
    @app.route('/user/<name>')
    def user(name):
        user = User.query.filter_by(username=name).first_or_404()
        return render_template('user.html', user=user)

    
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
        
    # Add this new route for registration
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        from .forms import RegistrationForm
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('index'))
        return render_template('register.html', title='Register', form=form)

    # Add a log-in route
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        from .forms import LoginForm  # Import the login form
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                # Redirect to the user's personal page after a successful login
                return redirect(url_for('user', name=user.username))
            else:
                flash('Login unsuccessful. Please check your username.', 'danger')
        return render_template('login.html', title='Login', form=form)


    # Return the configured app instance
    return app