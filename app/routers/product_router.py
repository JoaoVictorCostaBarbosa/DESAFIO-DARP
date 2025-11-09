from fastapi import APIRouter, status, Depends
from app.schemas.product_schema import ProductRequest, ProductResponse, ProductUpdateRequest
from app.services.product_service import ProductService
from app.schemas.user_schema import UserResponse
from app.core.dependencies import get_current_user, get_product_service
import uuid

router = APIRouter()

@router.post("/", response_model=ProductResponse)
async def create_product(
    product_data: ProductRequest,
    product_service: ProductService = Depends(get_product_service),
    current_user: UserResponse = Depends(get_current_user)
):
    return await product_service.create_product(product_data, current_user)

@router.get("/", response_model=list[ProductResponse])
async def get_all_products(
    product_service: ProductService = Depends(get_product_service),
):
    return await product_service.get_all_products()

@router.get("/{product_id}")
async def get_product_by_id(
    product_id: uuid.UUID,
    product_service: ProductService = Depends(get_product_service),
    current_user: UserResponse = Depends(get_current_user)
):
    return await product_service.get_product_by_id(product_id)

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: uuid.UUID,
    product_data: ProductUpdateRequest ,
    product_service: ProductService = Depends(get_product_service),
    current_user: UserResponse = Depends(get_current_user)
):
    return await product_service.update_product(product_data, product_id, current_user)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: uuid.UUID,
    product_service: ProductService = Depends(get_product_service),
    current_user: UserResponse = Depends(get_current_user)
):
    return await product_service.delete_product(product_id, current_user)
