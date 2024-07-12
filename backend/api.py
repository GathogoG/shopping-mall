from flask import Blueprint, request, jsonify
from .models import User, Product, Order, Payment, OrderProduct, db

api = Blueprint('api', __name__)

def error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response

@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'email', 'password')):
        return error_response('Missing data', 400)

    if User.query.filter_by(email=data['email']).first():
        return error_response('Email already exists', 400)

    user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@api.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return error_response('No input data', 400)

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    db.session.commit()
    return jsonify(user.to_dict())

@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

@api.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'price', 'stock')):
        return error_response('Missing data', 400)

    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@api.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())

@api.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return error_response('No input data', 400)

    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify(product.to_dict())

@api.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

@api.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data or not all(key in data for key in ('user_id', 'product_id', 'total_amount', 'status')):
        return error_response('Missing data', 400)

    order = Order(
        user_id=data['user_id'],
        total_amount=data['total_amount'],
        status=data['status']
    )
    db.session.add(order)
    db.session.commit()

    order_product = OrderProduct(order_id=order.id, product_id=data['product_id'], quantity=1)
    db.session.add(order_product)
    db.session.commit()

    return jsonify(order.to_dict()), 201

@api.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order.to_dict())

@api.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return error_response('No input data', 400)

    order.status = data.get('status', order.status)
    db.session.commit()
    return jsonify(order.to_dict())

@api.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

@api.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    if not data or not all(key in data for key in ('order_id', 'user_id', 'amount', 'payment_method')):
        return error_response('Missing data', 400)

    payment = Payment(
        order_id=data['order_id'],
        user_id=data['user_id'],
        amount=data['amount'],
        payment_method=data['payment_method']
    )
    db.session.add(payment)
    db.session.commit()
    return jsonify(payment.to_dict()), 201

@api.route('/payments/<int:id>', methods=['GET'])
def get_payment(id):
    payment = Payment.query.get_or_404(id)
    return jsonify(payment.to_dict())

@api.route('/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    payment = Payment.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return error_response('No input data', 400)

    payment.amount = data.get('amount', payment.amount)
    payment.payment_method = data.get('payment_method', payment.payment_method)
    payment.status = data.get('status', payment.status)
    db.session.commit()
    return jsonify(payment.to_dict())

@api.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    payment = Payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'Payment deleted successfully'}), 200

@api.route('/order_products', methods=['POST'])
def create_order_product():
    data = request.get_json()
    if not data or not all(key in data for key in ('order_id', 'product_id', 'quantity')):
        return error_response('Missing data', 400)

    order_product = OrderProduct(
        order_id=data['order_id'],
        product_id=data['product_id'],
        quantity=data['quantity']
    )
    db.session.add(order_product)
    db.session.commit()
    return jsonify(order_product.to_dict()), 201

@api.route('/order_products/<int:order_id>/<int:product_id>', methods=['GET'])
def get_order_product(order_id, product_id):
    order_product = OrderProduct.query.get_or_404((order_id, product_id))
    return jsonify(order_product.to_dict())

@api.route('/order_products/<int:order_id>/<int:product_id>', methods=['PUT'])
def update_order_product(order_id, product_id):
    order_product = OrderProduct.query.get_or_404((order_id, product_id))
    data = request.get_json()
    if not data:
        return error_response('No input data', 400)

    order_product.quantity = data.get('quantity', order_product.quantity)
    db.session.commit()
    return jsonify(order_product.to_dict())

@api.route('/order_products/<int:order_id>/<int:product_id>', methods=['DELETE'])
def delete_order_product(order_id, product_id):
    order_product = OrderProduct.query.get_or_404((order_id, product_id))
    db.session.delete(order_product)
    db.session.commit()
    return jsonify({'message': 'Order product deleted successfully'}), 200
