from app import app, db
from models import Product, CartItem

def seed_database():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

        # Clear existing products and cart items (optional)
        Product.query.delete()
        CartItem.query.delete()

        # Add sample products
        products = [
            Product(name='Car', description='Description for Car', price=909.99, stock_quantity=100),
            Product(name='Pen', description='Description for Pen', price=193.99, stock_quantity=50),
            Product(name='House', description='Description for House', price=279.99, stock_quantity=20)
        ]

        db.session.bulk_save_objects(products)  # Efficiently add multiple products
        db.session.commit()  # Commit the session

        # Add sample cart items (assuming product IDs correspond correctly)
        cart_items = [
            CartItem(product_id=1, quantity=2),  # Assuming product ID 1 exists
            CartItem(product_id=2, quantity=1)   # Assuming product ID 2 exists
        ]

        db.session.bulk_save_objects(cart_items)  # Efficiently add multiple cart items
        db.session.commit()  # Commit the session
        print("Database seeded with products and cart items!")

if __name__ == '__main__':
    seed_database()