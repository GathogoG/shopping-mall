from backend.app import create_app, db
from backend.models import User, Product, Order, Payment, OrderProduct

app = create_app()

with app.app_context():
    db.create_all()  

    # Add users
    user1 = User(name='Alice', email='alice@example.com', password='password1')
    user2 = User(name='Bob', email='bob@example.com', password='password2')
    user3 = User(name='Charlie', email='charlie@example.com', password='password3')
    user4 = User(name='David', email='david@example.com', password='password4')
    user5 = User(name='Eve', email='eve@example.com', password='password5')

    db.session.add_all([user1, user2, user3, user4, user5])
    db.session.commit()

    # Add products
    product1 = Product(name='Product 1', description='Description 1', price=10.0, stock=100)
    product2 = Product(name='Product 2', description='Description 2', price=20.0, stock=200)
    product3 = Product(name='Product 3', description='Description 3', price=30.0, stock=300)
    product4 = Product(name='Product 4', description='Description 4', price=40.0, stock=400)
    product5 = Product(name='Product 5', description='Description 5', price=50.0, stock=500)

    db.session.add_all([product1, product2, product3, product4, product5])
    db.session.commit()

    # Add orders
    order1 = Order(user_id=user1.id, status='Pending')
    order2 = Order(user_id=user2.id, status='Completed')
    order3 = Order(user_id=user3.id, status='Shipped')
    order4 = Order(user_id=user4.id, status='Delivered')
    order5 = Order(user_id=user5.id, status='Canceled')

    db.session.add_all([order1, order2, order3, order4, order5])
    db.session.commit()

    # Add payments
    payment1 = Payment(order_id=order1.id, user_id=user1.id, amount=100.0, payment_method='Credit Card')
    payment2 = Payment(order_id=order2.id, user_id=user2.id, amount=200.0, payment_method='PayPal')
    payment3 = Payment(order_id=order3.id, user_id=user3.id, amount=300.0, payment_method='Debit Card')
    payment4 = Payment(order_id=order4.id, user_id=user4.id, amount=400.0, payment_method='Credit Card')
    payment5 = Payment(order_id=order5.id, user_id=user5.id, amount=500.0, payment_method='PayPal')

    db.session.add_all([payment1, payment2, payment3, payment4, payment5])
    db.session.commit()

    # Add order products
    order_product1 = OrderProduct(order_id=order1.id, product_id=product1.id, quantity=1)
    order_product2 = OrderProduct(order_id=order2.id, product_id=product2.id, quantity=2)
    order_product3 = OrderProduct(order_id=order3.id, product_id=product3.id, quantity=3)
    order_product4 = OrderProduct(order_id=order4.id, product_id=product4.id, quantity=4)
    order_product5 = OrderProduct(order_id=order5.id, product_id=product5.id, quantity=5)

    db.session.add_all([order_product1, order_product2, order_product3, order_product4, order_product5])
    db.session.commit()
