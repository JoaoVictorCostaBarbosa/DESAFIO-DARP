from pydantic import BaseModel, Field, field_validator
from app.models.product import Product, Categories
import uuid

class ProductRequest(BaseModel):
    name: str = Field(min_length=3, max_length=100, description="Nome do produto entre 3 e 100 caracteres")
    description: str | None = Field(max_length=500, description="Descrição detalhada")
    price: float = Field(detail="Preço unitário (deve ser maior que 0)")
    quantity: int = Field(detail="Quantidade em estoque (deve ser maior ou igual a 0)")
    category: Categories = Field(detail="Categoria do produto (ex: 'frutas', 'laticínios')")
    localization: str | None = Field(detail="Localização do produto")

    def to_model(self, user_id: uuid.UUID) -> Product:
        return Product(
            name=self.name,
            description=self.description,
            price=self.price,
            quantity=self.quantity,
            category=self.category,
            localization=self.localization,
            user_id=user_id
        )

    @field_validator("price")
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError("O preço deve ser maior que 0")
        return v
    
    @field_validator("quantity")
    def validate_quantity(cls, v):
        if v < 0:
            raise ValueError("A quantidade deve ser maior ou igual a 0")
        return v

class ProductUpdateRequest(BaseModel):
    name: str | None = Field(min_length=3, max_length=100, description="Nome do produto entre 3 e 100 caracteres")
    description: str | None = Field(max_length=500, description="Descrição detalhada")
    price: float | None = Field(detail="Preço unitário (deve ser maior que 0)")
    quantity: int | None = Field(detail="Quantidade em estoque (deve ser maior ou igual a 0)")
    category: Categories | None = Field(detail="Categoria do produto (ex: 'frutas', 'laticínios')")
    localization: str | None = Field(detail="Localização do produto")

    def to_model(self, product: Product) -> Product:
        if self.name: product.name=self.name
        if self.description: product.description=self.description
        if self.price: product.price=self.price
        if self.quantity: product.quantity=self.quantity
        if self.category: product.category=self.category
        if self.localization: product.localization=self.localization

        return product

    @field_validator("price")
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError("O preço deve ser maior que 0")
        return v
    
    @field_validator("quantity")
    def validate_quantity(cls, v):
        if v < 0:
            raise ValueError("A quantidade deve ser maior ou igual a 0")
        return v

class ProductResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: str
    price: float
    quantity: int
    category: Categories
    localization: str
    user_id: uuid.UUID

    class Config:
        from_attributes = True