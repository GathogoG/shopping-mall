from app import app, db
from models import Product, CartItem

def seed_database():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

        # Clear existing products and cart items
        db.session.query(Product).delete()
        db.session.query(CartItem).delete()

        # Add sample products
        products = [
            Product(name='Car', description='Description for Car', price=909.99, stock_quantity=100, image_url='https://i.pinimg.com/474x/c0/b2/34/c0b234de7651f2e9de7c2a9578870909.jpg'),
            Product(name='Pen', description='Description for Pen', price=193.99, stock_quantity=50, image_url='https://www.pinterest.com/pin/746964288281587428/'),
            Product(name='House', description='Description for House', price=279.99, stock_quantity=20, image_url='https://i.pinimg.com/236x/23/78/bb/2378bb2b1e21fce6b3ae085cd462b121.jpg')
        ]

        db.session.bulk_save_objects(products)  # Efficiently add multiple products
        db.session.commit()  # Commit the session to get IDs for the products

        # Retrieve the products to ensure correct IDs
        car = Product.query.filter_by(name='Car').first()
        pen = Product.query.filter_by(name='Pen').first()

        # Add sample cart items using the retrieved product IDs
        cart_items = [
            CartItem(product_id=car.id, quantity=2),
            CartItem(product_id=pen.id, quantity=1)
        ]

        db.session.bulk_save_objects(cart_items)  # Efficiently add multiple cart items
        db.session.commit()  # Commit the session
        print("Database seeded with products and cart items!")

if __name__ == '__main__':
    seed_database()
