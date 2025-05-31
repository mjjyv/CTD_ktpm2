import pytest
from src.app import app
from src.database import init_db, db_session, Base, engine
from src.models import Product


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            # Drop and recreate tables to ensure clean state
            Base.metadata.drop_all(bind=engine)
            init_db()
            yield client
        db_session.remove()


def test_create_product(client):
    response = client.post("/products", json={"name": "Laptop", "price": 1000.0})
    assert response.status_code == 201
    assert response.json["name"] == "Laptop"
    assert response.json["price"] == 1000.0


def test_create_product_missing_data(client):
    response = client.post("/products", json={"name": "Laptop"})
    assert response.status_code == 400
    assert response.json["error"] == "Missing name or price"


def test_get_products(client):
    client.post("/products", json={"name": "Laptop", "price": 1000.0})
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Laptop"


def test_get_product(client):
    # Create product and get its ID
    create_response = client.post("/products", json={"name": "Laptop", "price": 1000.0})
    product_id = create_response.json["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json["name"] == "Laptop"


def test_get_product_not_found(client):
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json["error"] == "Product not found"


def test_update_product(client):
    # Create product and get its ID
    create_response = client.post("/products", json={"name": "Laptop", "price": 1000.0})
    product_id = create_response.json["id"]
    response = client.put(
        f"/products/{product_id}", json={"name": "Updated Laptop", "price": 1200.0}
    )
    assert response.status_code == 200
    assert response.json["name"] == "Updated Laptop"
    assert response.json["price"] == 1200.0


def test_delete_product(client):
    # Create product and get its ID
    create_response = client.post("/products", json={"name": "Laptop", "price": 1000.0})
    product_id = create_response.json["id"]
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json["message"] == "Product deleted"
