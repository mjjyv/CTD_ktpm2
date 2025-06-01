from flask import Flask, request, jsonify
from src.models import Product
from src.database import init_db, db_session

app = Flask(__name__)

# Khởi tạo database
init_db()


@app.teardown_appcontext
def shutdown_session():
    """Close the database session after each request."""
    db_session.remove()


@app.route("/products", methods=["POST"])
def create_product():
    """Create a new product."""
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "price")):
        return jsonify({"error": "Missing name or price"}), 400
    product = Product(name=data["name"], price=data["price"])
    db_session.add(product)
    db_session.commit()
    return (
        jsonify({"id": product.id, "name": product.name, "price": product.price}),
        201,
    )


@app.route("/products", methods=["GET"])
def get_products():
    """Retrieve all products."""
    products = Product.query.all()
    return (
        jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products]),
        200,
    )


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieve a product by ID."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 200


@app.route("/products/<int:id>", methods=["PUT"])
def update_product(product_id):
    """Update a product by its ID."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "price")):
        return jsonify({"error": "Missing name or price"}), 400
    product.name = data["name"]
    product.price = data["price"]
    db_session.commit()
    return (
        jsonify({"id": product.product_id, "name": product.name, "price": product.price}),
        200,
    )


@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete a product by its ID."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    db_session.delete(product)
    db_session.commit()
    return jsonify({"message": "Product deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
