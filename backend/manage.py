from flask import Flask
from flask_migrate import Migrate
from backend.models import db
from backend.api import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping-mall.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '360b1c5f493e9b6d9a1fef7c2a85d8a1b620a29c8a2f46f2a28a'
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True) 
