from fastapi import APIRouter, status, Depends
from app.schemas.user_schema import UserResponse, UserUpdate
from app.services.user_service import UserService
from app.core.dependencies import get_current_user, get_user_service
import uuid

router = APIRouter()

@router.get("/", response_model=list[UserResponse])
async def get_users(
    user_service: UserService = Depends(get_user_service),
    current_user: UserResponse = Depends(get_current_user)
):
    return await user_service.get_all_users(current_user)

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: uuid.UUID,
    user_data: UserUpdate,
    user_service: UserService = Depends(get_user_service),
    current_user: UserResponse = Depends(get_current_user)    
):
    return await user_service.update_user(user_data, user_id, current_user)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: uuid.UUID,
    user_service: UserService = Depends(get_user_service),
    current_user: UserResponse = Depends(get_current_user)
):
    return await user_service.delete_user(user_id, current_user)