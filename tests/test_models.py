import pytest
from src.models import Product
from src.database import init_db, db_session, Base, engine


@pytest.fixture
def setup_db():
    """Set up a clean database for testing."""
    Base.metadata.drop_all(bind=engine)
    init_db()
    yield
    db_session.remove()


def test_product_creation(setup_db):
    """Test creating a product in the database."""
    product = Product(name="Laptop", price=1000.0)
    db_session.add(product)
    db_session.commit()
    assert product.id is not None
    assert product.name == "Laptop"
    assert product.price == 1000.0
