from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Product, CartItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Create all tables
with app.app_context():
    db.create_all()

# Route to fetch all items in the cart
@app.route('/cart', methods=['GET'])
def get_cart_items():
    cart_items = CartItem.query.all()
    cart_list = [{
        'id': item.id,
        'product_id': item.product_id,
        'quantity': item.quantity,
        'product_name': item.product.name,
        'price': item.product.price
    } for item in cart_items]
    return jsonify({'cart_items': cart_list})

# Route to add an item to the cart
@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    new_cart_item = CartItem(
        product_id=data['product_id'],
        quantity=data['quantity']
    )
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify({'message': 'Item added to cart!', 'item_id': new_cart_item.id}), 201

# Route to remove an item from the cart
@app.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    cart_item = CartItem.query.get(item_id)
    if not cart_item:
        return jsonify({'message': 'Cart item not found!'}), 404
    
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item removed from cart!'})

if __name__ == '__main__':
    app.run(debug=True)
