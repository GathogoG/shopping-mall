from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from . import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    orders = relationship('Order', back_populates='user')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at
        }

class Product(db.Model):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'stock': self.stock,
            'created_at': self.created_at
        }

class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(TIMESTAMP, default=datetime.utcnow)
    status = Column(String, nullable=False)
    
    user = relationship('User', back_populates='orders')
    order_products = relationship('OrderProduct', back_populates='order')
    payments = relationship('Payment', back_populates='order')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'order_date': self.order_date,
            'status': self.status,
            'products': [op.product.to_dict() for op in self.order_products],
            'payments': [payment.to_dict() for payment in self.payments]
        }

class Payment(db.Model):
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    payment_date = Column(TIMESTAMP, default=datetime.utcnow)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(String, nullable=False)
    
    order = relationship('Order', back_populates='payments')

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'user_id': self.user_id,
            'payment_date': self.payment_date,
            'amount': str(self.amount),
            'payment_method': self.payment_method
        }

class OrderProduct(db.Model):
    __tablename__ = 'order_products'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)

    order = relationship('Order', back_populates='order_products')
    product = relationship('Product')

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'product': self.product.to_dict()
        }
