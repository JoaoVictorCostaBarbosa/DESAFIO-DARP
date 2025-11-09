from fastapi import APIRouter, status, Depends
from app.schemas.user_schema import UserCreate, UserLogin, UserTokenResponse
from app.services.auth_service import AuthService
from app.core.dependencies import get_auth_service

router = APIRouter()

@router.post("/register", response_model=UserTokenResponse)
async def register(
    user_data: UserCreate,
    auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.create_user(user_data)

@router.post("/login", response_model=UserTokenResponse)
async def login(
    user_data: UserLogin,
    auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.login(user_data)
