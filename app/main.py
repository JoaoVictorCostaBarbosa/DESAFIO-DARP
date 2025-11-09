from fastapi import FastAPI
from app.routers import auth_router, user_router, product_router

app = FastAPI(title="Marketplace Agro", version="0.1.0")

app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user_router.router, prefix="/api/v1/users", tags=["user"])
app.include_router(product_router.router, prefix="/api/v1/products", tags=["product"])

@app.get("/")
async def root():
    return {"message": "Marketplace Agro está rodando"}
