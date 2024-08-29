import os
from flask import Flask, render_template, redirect, url_for, flash, jsonify, request
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5 # Import the Bootstrap class from the flask_bootstrap package
from dotenv import load_dotenv # Import the load_dotenv function from the dotenv module
from .models import db  # Import the database object from the models package
from config import Config # Import the Config class from the config module
from sqlalchemy import inspect
from flask_login import LoginManager, login_required, current_user,login_user
from .models import Document

# migrate can be used to create and manage database migrations
migrate = Migrate()

def create_app():
    # Load environment variables from a .env file
    load_dotenv()  
    # Initialize the Flask app with necessary configurations & extensions
    app = Flask(__name__)
    # Apply configuration settings from config.py with class Config
    app.config.from_object(Config)
    # Initialize Bootstrap with the app
    Bootstrap5(app)
    # Initialize the app with the database
    db.init_app(app)
    # Initialize the app with the migration
    migrate.init_app(app, db)

    # Import your models and create the database tables
    # the app.app_context() function allows you to run code within the application context
    with app.app_context():
        from .models import User  # Import all models
        db.create_all()  # Create tables for all models

    # Set template and static folders
    # The code's ../../.. mean that the path is going up three directories from the current file
    app.template_folder = os.path.abspath(os.path.join(__file__, '../../../frontend/templates'))
    app.static_folder = os.path.abspath(os.path.join(__file__, '../../../frontend/static'))

    # Initialize Flask-Login
    login_manager = LoginManager()
    # Initialize the login manager with the app
    login_manager.init_app(app)
    # Set the login view to the login route
    login_manager.login_view = 'login'  # Specify what view to redirect to when login is required
    # Set the login message category
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    # Define routes (you can move these to a separate file later if desired)
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Add a new route for user pages
    @app.route('/user/<name>')
    def user(name):
        # Query (i.e: SELECT) the database for a user with the given username
        # The function User.query.filter_by(username=name) is equivalent to SELECT * FROM user WHERE username=name
        # The function first_or_404() returns the first result of the query or a 404 error if no results are found
        user = User.query.filter_by(username=name).first_or_404()
        # Query the database for all documents created by the user
        user_documents = Document.query.filter_by(user_id=user.id).all()
        # Render the user.html template with the user and documents
        return render_template('user.html', user=user, documents=user_documents)
       

    # Add a test route
    @app.route('/test')
    def test():
        # Render the test.html template
        return render_template('test.html')
    # Test whether the database connection is successful
    @app.route('/test_db')
    def test_db():
        # Try to query the database for the first user
        try:
            # The function query(User) is equivalent to SELECT * FROM user
            db.session.query(User).first()
            return "Database connection successful!"
        # If an exception is raised, return an error message
        except Exception as e:
            return f"Database connection failed: {str(e)}"
        
    # Add this new route for registration
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        # Import the RegistrationForm class from the forms module
        from .forms import RegistrationForm
        # Create an instance of the RegistrationForm
        form = RegistrationForm()
        # If the form is submitted and valid, create a new user
        if form.validate_on_submit():
            # Create a new user adding the form data
            user = User(username=form.username.data, email=form.email.data)
            # This function is equivalent to INSERT INTO user (username, email) VALUES (form.username.data, form.email.data)
            db.session.add(user)
            # This function is equivalent to COMMIT
            db.session.commit()
            # Flash a success message, the flash() function is used to display a message to the user
            flash('Congratulations, you are now a registered user!')
            # Redirect the user to the index page. The url_for() function generates the URL for the index route
            return redirect(url_for('index'))
        # Render the register.html template with the form object
        return render_template('register.html', title='Register', form=form)

    # Add a new route for login
    @app.route('/login', methods=['GET', 'POST'])
    # Define the login function
    def login():
        # Import the LoginForm class from the forms module
        from .forms import LoginForm
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                # login_user() is a function from Flask-Login that logs in the user
                login_user(user)
                flash('Logged in successfully.', 'success')
                return redirect(url_for('user', name=user.username))
            else:
                flash('Login unsuccessful. Please check your username.', 'danger')
        return render_template('login.html', title='Login', form=form)
    
    # Add a route to display the database structure
    @app.route('/db_structure')
    def db_structure():
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        structure = {}
        for table in tables:
            columns = [{
                'name': column['name'],
                'type': str(column['type']),
                'nullable': column['nullable']
            } for column in inspector.get_columns(table)]
            structure[table] = columns
        return jsonify(structure)
    

    @app.route('/documents')
    @login_required
    def documents():
        user_documents = Document.query.filter_by(user_id=current_user.id).all()
        return render_template('document.html', documents=user_documents)

    @app.route('/create_document', methods=['GET', 'POST'])
    @login_required
    def create_document():
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            if title:
                new_document = Document(title=title, content=content, user_id=current_user.id)
                db.session.add(new_document)
                db.session.commit()
                flash('Document created successfully!', 'success')
                return redirect(url_for('documents'))
        return render_template('create_document.html')
    
    @app.route('/view_document/<int:id>', methods=['GET', 'POST'])
    @login_required
    def view_document(id):
        document = Document.query.get_or_404(id)
        if document.user_id != current_user.id:
            flash('You do not have permission to view this document.', 'danger')
            return redirect(url_for('documents'))
        
        if request.method == 'POST':
            document.title = request.form.get('title')
            document.content = request.form.get('content')
            db.session.commit()
            flash('Document updated successfully!', 'success')
            return redirect(url_for('view_document', id=document.id))
        
        return render_template('view_document.html', document=document)

    @app.route('/delete_document/<int:id>', methods=['POST'])
    @login_required
    def delete_document(id):
        document = Document.query.get_or_404(id)
        if document.user_id != current_user.id:
            flash('You do not have permission to delete this document.', 'danger')
        else:
            db.session.delete(document)
            db.session.commit()
            flash('Document deleted successfully!', 'success')
        return redirect(url_for('documents'))
    



    # Return the configured app instance
    return app