from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models.product import Categories, Product
import uuid

class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_product(
        self,
        product: Product,
    ) -> Product:
        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)

        return product
    
    async def get_all_products(self) -> list[Product]:
        products = await self.db.execute(select(Product))

        return list(products.scalars().all())
    
    async def get_product_by_id(self, product_id: uuid.UUID) -> Product | None:
        product = await self.db.execute(select(Product).where(Product.id == product_id))

        return product.scalar_one_or_none()
    
    async def update_product(self, product: Product) -> Product:
        await self.db.execute(
            update(Product)
            .where(Product.id == product.id)
            .values(
                name = product.name,
                description = product.description,
                price = product.price,
                quantity = product.quantity,
                category = product.category,
                localization = product.localization
            )
        )

        await self.db.commit()

        result = await self.db.execute(select(Product).where(Product.id == product.id))
        
        return result.scalar_one()
    
    async def delete_product(self, product: Product):
        await self.db.delete(product)
        await self.db.commit()
