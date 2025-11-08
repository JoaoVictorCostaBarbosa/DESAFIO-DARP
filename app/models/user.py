from sqlalchemy import Column, String, Enum as sqlalchemyEnum
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
from enum import Enum
import uuid

class UserRole(str, Enum):
    admin = "admin"
    producer = "produtor"
    buyer = "comprador"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), index=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    hash_password = Column(String, index=True, nullable=False)
    userType = Column(sqlalchemyEnum(UserRole), index=True, nullable=False)
    localization = Column(String(100), index=True)
