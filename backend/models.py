from sqlalchemy import create_engine, Column, Integer, String, Text, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from config import DATABASE_URI

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    
    orders = relationship('Order', back_populates='user')

class Product(Base):
    __tablename__ = 'products'
    
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    order_date = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String(255), nullable=False)
    
    user = relationship('User', back_populates='orders')
    payments = relationship('Payment', back_populates='order')

class Payment(Base):
    __tablename__ = 'payments'
    
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    method = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False)
    
    order = relationship('Order', back_populates='payments')

def setup_database():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
    return engine

if __name__ == "__main__":
    engine = setup_database()
    print("Database tables created")

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

