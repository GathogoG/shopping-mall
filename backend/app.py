from flask_migrate import Migrate
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



migrate = Migrate(app, db)

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)


@app.route('/users', methods=['GET'])
def get_users():


    users = User.query.all()

    result = []
# Example route
@app.route('/')
def index():
    return 'Welcome to the shopping site!'

if __name__ == '__main__':
    app.run(debug=True)
