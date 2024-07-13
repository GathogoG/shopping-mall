from app import app, db
from models import Product

def seed_database():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

        # Clear existing products (optional)
        Product.query.delete()

        # Add sample products
        products = [
            Product(name='car', description='Description for Product car', price=909.99, stock_quantity=100),
            Product(name='Pen', description='Description for Product pen', price=193.99, stock_quantity=50),
            Product(name='house', description='Description for Product house', price=279.99, stock_quantity=20)
        ]

        db.session.bulk_save_objects(products)  # Efficiently add multiple products
        db.session.commit()  # Commit the session
        print("Database seeded with products!")

if __name__ == '__main__':
    seed_database()
