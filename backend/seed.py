# seed.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, User ,Product # Import your models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def seed_database():
    with app.app_context():
        # Create a new user
        new_user = User(username='john_doe', email='john@example.com', password_hash='hashed_password')

        # Create product
        Product(name='Product 2', description='Description 2', price=15.0, stock_quantity=50)

        # Add the new user to the session
        db.session.add(new_user)

        # Commit the session to persist the new user in the database
        db.session.commit()

# if __name__ == '__main__':
#     seed_database()
