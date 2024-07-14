from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Product, CartItem, Order, OrderItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Route to fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock_quantity': product.stock_quantity,
        'image_url': product.image_url
    } for product in products]
    return jsonify({'products': product_list})

# Route to view cart items
@app.route('/cart', methods=['GET'])
def view_cart():
    cart_items = CartItem.query.all()
    cart_list = [{
        'id': item.id,
        'product_id': item.product_id,
        'quantity': item.quantity,
        'product': {
            'name': item.product.name,
            'description': item.product.description,
            'price': item.product.price,
            'image_url': item.product.image_url
        }
    } for item in cart_items]
    return jsonify({'cart_items': cart_list})

# Route to add an item to the cart
@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    if product.stock_quantity < quantity:
        return jsonify({'error': 'Not enough stock'}), 400
    cart_item = CartItem.query.filter_by(product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item added to cart'})

# Route to remove an item from the cart
@app.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    cart_item = CartItem.query.get(item_id)
    if not cart_item:
        return jsonify({'error': 'Item not found in cart'}), 404
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item removed from cart'})

# Route to create an order
@app.route('/orders', methods=['POST'])
def create_order():
    cart_items = CartItem.query.all()
    if not cart_items:
        return jsonify({'error': 'Cart is empty'}), 400
    
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    order = Order(total_amount=total_amount, status='Pending')
    db.session.add(order)
    db.session.commit()

    order_items = [
        OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity, unit_price=item.product.price)
        for item in cart_items
    ]
    db.session.bulk_save_objects(order_items)
    db.session.commit()

    # Clear the cart after order is placed
    CartItem.query.delete()
    db.session.commit()

    return jsonify({'message': 'Order placed successfully', 'order_id': order.id})

# Route to view all orders
@app.route('/orders', methods=['GET'])
def view_orders():
    orders = Order.query.all()
    order_list = [{
        'id': order.id,
        'order_date': order.order_date,
        'total_amount': order.total_amount,
        'status': order.status,
        'items': [{
            'product_id': item.product_id,
            'product_name': item.product.name,
            'quantity': item.quantity,
            'unit_price': item.unit_price
        } for item in order.items]
    } for order in orders]
    return jsonify({'orders': order_list})

if __name__ == '__main__':
    app.run(port=5555)
    app.run(debug=True)
