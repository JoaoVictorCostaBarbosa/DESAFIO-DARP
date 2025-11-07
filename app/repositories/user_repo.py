from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models.user import User, UserRole
import uuid

class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: User) -> User:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user
    
    async def get_user_by_id(self, id: uuid.UUID) -> User | None:
        result = await self.db.execute(select(User).where(User.id == id))

        return result.scalar_one_or_none
    
    async def get_user_by_email(self, email: str) -> User | None:
        result = await self.db.execute(select(User).where(User.email == email))
        
        return result.scalar_one_or_none()
    
    async def get_all_users_by_user_type(self, type: UserRole) -> list[User]:
        result = await self.db.execute(select(User).where(User.userType == type))

        return list(result.scalars.all())
    
    async def get_all_users(self) -> list[User]:
        result = await self.db.execute(select(User))

        return list(result.scalars.all())
    
    async def update_user(self, user: User, id: uuid.UUID):
        await self.db.execute(
            update(User)
            .where(User.id == id)
            .values(
                name=user.name,
                email=user.email,
                localization=user.localization
            )
        )

        await self.db.commit()

    async def delete_user(self, user: User):
        await self.db.delete(User)
        await self.db.commit()
