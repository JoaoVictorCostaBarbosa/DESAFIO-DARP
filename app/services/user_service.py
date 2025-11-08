from fastapi import HTTPException, status
from app.schemas.user_schema import UserResponse, UserUpdate
from app.repositories.user_repo import UserRepository
from app.models.user import UserRole
import uuid

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_all_users(
        self,
        current_user: UserResponse
    ) -> list[UserResponse]:
        if current_user.userType != UserRole.admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Soemnte admins podem verificar todos os usuários"
            )
        
        users = await self.user_repo.get_all_users()

        return users

    async def update_user(
        self,
        user_data: UserUpdate,
        user_id: uuid.UUID,
        current_user: UserResponse
    ) -> UserResponse:
        user = await self.user_repo.get_user_by_id(user_id)

        if current_user.userType != UserRole.admin and current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Somente admins podem atualizar podem atualizar outros usuários"
            )
        
        updated_user = await self.user_repo.update_user(user_data.to_model(user), user_id)

        return updated_user
    
    async def delete_user(
        self,
        user_id: uuid.UUID,
        current_user: UserResponse
    ) -> status:
        user = await self.user_repo.get_user_by_id(user_id)

        if current_user.userType != UserRole.admin:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Somente admins podem deletar usuários"
            )
        
        await self.user_repo.delete_user(user)

        return status.HTTP_204_NO_CONTENT
    