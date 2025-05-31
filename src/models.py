from sqlalchemy import Column, Integer, String, Float
from src.database import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price})>"
