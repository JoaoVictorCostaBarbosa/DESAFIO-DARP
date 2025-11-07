from pydantic import BaseModel, EmailStr, Field, field_validator
from app.models.user import UserRole
from app.models.user import User
import uuid
import re

PASSWORD_PATTERN = r"^(?=.*[a-zA-Z])(?=.*\d).{8,}$"

class UserCreate(BaseModel):
    name: str = Field(min_length=3, description="Nome do usuário com no mínimo 3 caracteres")
    email: EmailStr = Field(description="Email válido")
    password: str = Field(description="Senha com no mínimo 8 caracteres, contendo letras e números")
    userType: UserRole = Field(description="Permissões do usuário ('produtor', 'comprador' ou 'admin')")
    localization: str = Field(max_length=100 ,description="Cidade/Região do usuário")

    def to_model(self, hashed_password) -> User:
        return User(
            name=self.name,
            email=self.email,
            hash_password=hashed_password,
            userType=self.userType,
            localization=self.localization
        )
    
    @field_validator("password")
    def validate_password(cls, v):
        if not re.match(PASSWORD_PATTERN, v):
            raise ValueError("A senha deve ter no mínimo 8 caracteres e conter letras e números.")
        return v

class UserLogin(BaseModel):
    email: EmailStr = Field(description="Email válido")
    password: str = Field(description="Senha")

class UserUpdate(BaseModel):
    name: str = Field(min_length=3, description="Nome do usuário com no mínimo 3 caracteres")
    email: EmailStr = Field(description="Email válido")
    localization: str = Field(max_length=100 ,description="Cidade/Região do usuário")

class UserResponse(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    userType: UserRole
    localization: str

    class Config:
        from_attributes = True

class UserTokenResponse(BaseModel):
    user: UserResponse
    token: str