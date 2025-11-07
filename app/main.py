from fastapi import FastAPI
from app.routers import auth_routers

app = FastAPI(title="Marketplace Agro", version="0.1.0")

app.include_router(auth_routers.router, prefix="/api/v1/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Marketplace Agro está rodando"}
