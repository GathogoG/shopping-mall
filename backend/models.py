# from app import db
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

metadata = MetaData() 

db = SQLAlchemy(metadata  = metadata) 

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

class Order(db.Model):

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    # user = db.relationship('User', backref=db.backref('orders', lazy=True))

class OrderItem(db.Model):

    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    # order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    order = db.relationship('Order', backref=db.backref('items', lazy=True))
    product = db.relationship('Product', backref=db.backref('order_items', lazy=True))

if __name__ == '__main__':
    # This block will be executed if you run `python models.py` directly
    db.create_all()
