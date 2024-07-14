import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, Product, CartItem, Order, OrderItem, Payment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize CORS
CORS(app)

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Configure logging
if not app.debug:
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock_quantity': product.stock_quantity,
            'image_url': product.image_url
        }
        product_list.append(product_data)
    return jsonify({'products': product_list})

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    product = Product.query.get(product_id)
    if product and product.stock_quantity >= quantity:
        cart_item = CartItem(product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
        product.stock_quantity -= quantity
        db.session.commit()
        return jsonify({'message': 'Item added to cart successfully!'})
    else:
        return jsonify({'message': 'Item is out of stock!'}), 400

if __name__ == '__main__':
    app.run(port=5555)
    app.run(debug=True)
