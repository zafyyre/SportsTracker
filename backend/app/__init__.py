# backend/app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the database object (SQLAlchemy)
db = SQLAlchemy()

def create_app():
    """
    Application factory function. This function is called to create an instance of the Flask application.
    Using an application factory allows for easy configuration and testing.
    """
    # Create an instance of the Flask class
    app = Flask(__name__)
    
    # Set configuration variables
    # These configurations are necessary for connecting to the SQLite database
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../sports.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with the app instance
    # db.init_app binds the database to the app instance
    db.init_app(app)
    
    # Enable Cross-Origin Resource Sharing (CORS)
    # This allows your app to handle requests from different domains
    CORS(app)

    # Create the application context and initialize the database
    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy
        from .models import Soccer, Basketball, Hockey  # Importing the database tables

        # Create all database tables
        db.create_all()

        # Import routes after the app context is pushed
        from . import routes # Importing the entire routes module

    # Return the Flask app instance
    # This instance will be used to run the application
    return app
