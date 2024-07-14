from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)

@app.route('/place_order', methods=['POST'])
def place_order():
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']

    product = Product.query.get(product_id)

    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    if product.stock_quantity < quantity:
        return jsonify({'error': 'Not enough stock available'}), 400

    # Adjust stock quantity
    product.stock_quantity -= quantity
    db.session.commit()

    # Create the order
    total_amount = product.price * quantity
    order = Order(total_amount=total_amount, status='Pending')
    db.session.add(order)
    db.session.commit()

    # Add the order item
    order_item = OrderItem(order_id=order.id, product_id=product_id, quantity=quantity, unit_price=product.price)
    db.session.add(order_item)
    db.session.commit()

    return jsonify({'message': 'Order placed successfully', 'order_id': order.id}), 200

if __name__ == '__main__':
    app.run(debug=True)
