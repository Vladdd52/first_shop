from venv import create
from ..database import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, DateTime
from datetime import datetime, timezone  


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    price = Column(Float , nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price}, category_id={self.category_id})>"