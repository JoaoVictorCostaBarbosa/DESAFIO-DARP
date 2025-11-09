from sqlalchemy import Column, String, Numeric, ForeignKey, Enum as sqlachemyEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from enum import Enum
from app.db.base import Base
import uuid

class Categories(str, Enum):
    fruits = "frutas"
    grains = "grãos"
    dairy = "laticínios"
    others = "outros"

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), index=True, nullable=False)
    description = Column(String(500), index=True)
    price = Column(Numeric(10, 2), index=True, nullable=False)
    quantity = Column(Numeric, index=True, nullable=False)
    category = Column(sqlachemyEnum(Categories), index=True, nullable=False)
    localization = Column(String, index=True)
    user_id = Column(UUID, ForeignKey("users.id"), index=True)

    user = relationship("User", back_populates="products")