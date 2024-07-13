from app import app, db
from models import Product

def seed_database():
    with app.app_context():
        db.create_all()  # Create tables if not already created
        # Add sample products
        product1 = Product(name='Product 1', description='Description for Product 1', price=9.99, stock_quantity=100)
        product2 = Product(name='Product 2', description='Description for Product 2', price=19.99, stock_quantity=50)
        
        db.session.add(product1)
        db.session.add(product2)
        db.session.commit()
        print("Database seeded!")

if __name__ == '__main__':
    seed_database()
