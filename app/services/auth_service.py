from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schema import UserCreate, UserLogin, UserTokenResponse
from app.repositories.user_repo import UserRepository
from app.core.security import verify_password, hash_password, create_access_token

class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user_data: UserCreate) -> UserTokenResponse:
        existing_user = await self.user_repo.get_user_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email já registrado"
            )
        
        hashed_password = hash_password(user_data.password)
        
        user = await self.user_repo.create_user(user_data.to_model(hashed_password))
        access_token = create_access_token(data={"sub": user.email, "user_id": user.id})

        return UserTokenResponse(user=user, token=access_token)
    
    async def login(self, user_data: UserLogin) -> UserTokenResponse:
        user = await self.user_repo.get_user_by_email(user_data.email)

        if not user or not verify_password(user_data.password, user.hash_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas"
            )

        access_token = create_access_token(data={"sub": user.email, "user_id": user.id})

        return UserTokenResponse(user=user, token=access_token)
