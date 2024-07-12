from flask import Flask
from flask_migrate import Migrate, upgrade, init, migrate
from backend.models import db, User, Product, Order, Payment, OrderProduct

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping-mall.db'
db.init_app(app)

migrate = Migrate(app, db)

@app.cli.command('setup')
def setup():
    """Initialize database, run migrations, and seed the database."""
    print("Initializing migrations...")
    try:
        init()
        print("Migrations initialized.")
    except Exception as e:
        print(f"Error initializing migrations: {e}")

    print("Generating migrations...")
    try:
        migrate(message="Auto-generated migration")
        print("Migrations generated.")
    except Exception as e:
        print(f"Error generating migrations: {e}")

    print("Applying migrations...")
    try:
        upgrade()
        print("Migrations applied.")
    except Exception as e:
        print(f"Error applying migrations: {e}")

    print("Seeding the database...")
    with app.app_context():
        db.create_all()

        users = [
            User(name='Alice', email='alice@example.com', password='password1'),
            User(name='Bob', email='bob@example.com', password='password2'),
            User(name='Charlie', email='charlie@example.com', password='password3'),
            User(name='David', email='david@example.com', password='password4'),
            User(name='Eve', email='eve@example.com', password='password5')
        ]
        db.session.bulk_save_objects(users)
        db.session.commit()

        products = [
            Product(name='Product 1', description='Description 1', price=10.0, stock=100),
            Product(name='Product 2', description='Description 2', price=20.0, stock=200),
            Product(name='Product 3', description='Description 3', price=30.0, stock=300),
            Product(name='Product 4', description='Description 4', price=40.0, stock=400),
            Product(name='Product 5', description='Description 5', price=50.0, stock=500)
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()

        orders = [
            Order(user_id=1, status='Pending'),
            Order(user_id=2, status='Completed'),
            Order(user_id=3, status='Shipped'),
            Order(user_id=4, status='Delivered'),
            Order(user_id=5, status='Canceled')
        ]
        db.session.bulk_save_objects(orders)
        db.session.commit()

        payments = [
            Payment(order_id=1, user_id=1, amount=100.0, payment_method='Credit Card'),
            Payment(order_id=2, user_id=2, amount=200.0, payment_method='PayPal'),
            Payment(order_id=3, user_id=3, amount=300.0, payment_method='Debit Card'),
            Payment(order_id=4, user_id=4, amount=400.0, payment_method='Credit Card'),
            Payment(order_id=5, user_id=5, amount=500.0, payment_method='PayPal')
        ]
        db.session.bulk_save_objects(payments)
        db.session.commit()

        order_products = [
            OrderProduct(order_id=1, product_id=1, quantity=1),
            OrderProduct(order_id=2, product_id=2, quantity=2),
            OrderProduct(order_id=3, product_id=3, quantity=3),
            OrderProduct(order_id=4, product_id=4, quantity=4),
            OrderProduct(order_id=5, product_id=5, quantity=5)
        ]
        db.session.bulk_save_objects(order_products)
        db.session.commit()

    print("Setup complete!")

if __name__ == '__main__':
    app.run()
