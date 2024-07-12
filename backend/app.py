from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend.config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
  
    from backend.models import User, Product, Order, Payment, OrderProduct

    print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])
    print("Models imported:", User, Product, Order, Payment, OrderProduct)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
