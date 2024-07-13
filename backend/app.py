from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Create all tables
with app.app_context():
    db.create_all()

# Route to fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock_quantity': product.stock_quantity
    } for product in products]
    return jsonify({'products': product_list})

# Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        stock_quantity=data['stock_quantity']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully!', 'product': {'id': new_product.id}}), 201

# Route to update an existing product
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found!'}), 404
    
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
    
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})

# Route to delete a product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found!'}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
