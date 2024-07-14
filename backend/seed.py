# seed.py
from app import app, db
from models import Product, CartItem, Order, OrderItem, Payment
from flask import current_app

def seed_database():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

        # Clear existing products, cart items, orders, order items, and payments (optional)
        Product.query.delete()
        CartItem.query.delete()
        OrderItem.query.delete()
        Order.query.delete()
        Payment.query.delete()

        # Add sample products
        products = [
            Product(name='Car', description='Description for Car', price=909.99, stock_quantity=100, image_url='https://i.pinimg.com/474x/c0/b2/34/c0b234de7651f2e9de7c2a9578870909.jpg'),
            Product(name='Pen', description='Description for Pen', price=193.99, stock_quantity=50, image_url='https://www.pinterest.com/pin/746964288281587428/'),
            Product(name='House', description='Description for House', price=279.99, stock_quantity=20, image_url='https://i.pinimg.com/236x/23/78/bb/2378bb2b1e21fce6b3ae085cd462b121.jpg')
        ]

        db.session.bulk_save_objects(products)  # Efficiently add multiple products
        db.session.commit()  # Commit the session

        # Retrieve products to ensure IDs are correct
        car = Product.query.filter_by(name='Car').first()
        pen = Product.query.filter_by(name='Pen').first()

        # Add sample cart items
        cart_items = [
            CartItem(product_id=car.id, quantity=2),  # Using the correct product ID
            CartItem(product_id=pen.id, quantity=1)   # Using the correct product ID
        ]

        db.session.bulk_save_objects(cart_items)  # Efficiently add multiple cart items
        db.session.commit()  # Commit the session

        # Calculate total amount from cart items
        total_amount = sum(item.quantity * db.session.get(Product, item.product_id).price for item in cart_items)

        # Create a sample order
        order = Order(total_amount=total_amount, status='Pending')
        db.session.add(order)
        db.session.commit()

        order_items = [
            OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity, unit_price=db.session.get(Product, item.product_id).price)
            for item in cart_items
        ]
        db.session.bulk_save_objects(order_items)
        db.session.commit()

        # Clear the cart after order is placed
        CartItem.query.delete()
        db.session.commit()

        # Process a sample payment
        payment = Payment(order_id=order.id, amount=order.total_amount, payment_method='Credit Card', status='Completed')
        db.session.add(payment)
        order.status = 'Paid'
        db.session.commit()

        print("Database seeded with products, cart items, order, and payment!")

if __name__ == '__main__':
    seed_database()
