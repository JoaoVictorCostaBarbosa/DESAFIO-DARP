from fastapi import HTTPException, status
from app.repositories.product_repo import ProductRepository
from app.schemas.product_schema import ProductRequest, ProductResponse, ProductUpdateRequest
from app.schemas.user_schema import UserResponse
from app.models.user import UserRole
from app.models.product import Categories
import uuid

class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def create_product(self, product_data: ProductRequest, current_user: UserResponse) -> ProductResponse:
        if current_user.userType != UserRole.producer:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Somente produtores podem cadastrar novos produtos"
            )
        
        product = await self.product_repo.create_product(product_data.to_model(current_user.id))

        return product
    
    async def get_all_products(self) -> list[ProductResponse]:
        products = await self.product_repo.get_all_products()

        return products

    async def get_product_by_id(self, product_id: uuid.UUID) -> ProductResponse:
        product = await self.product_repo.get_product_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )
        
        return product
    
    async def update_product(
        self, 
        product_data: ProductUpdateRequest, 
        product_id: uuid.UUID,
        current_user: UserResponse
    ) -> ProductResponse:
        
        product = await self.product_repo.get_product_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )
        
        if product.user_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Somente o dono do produto pode atualizar ele"
            )
        
        updated_product = await self.product_repo.update_product(product_data.to_model(product))

        return updated_product
    
    async def delete_product(self, product_id: uuid.UUID, current_user: UserResponse) -> status:
        product = await self.product_repo.get_product_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Produto não encontrado"
            )

        if product.user_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Somente o dono do produto pode apagar ele"
            )
        
        await self.product_repo.delete_product(product)