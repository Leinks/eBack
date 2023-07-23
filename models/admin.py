from typing import Optional
from beanie import Document
from datetime import datetime
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr

class Admin(Document):
    name: Optional[str]
    email: EmailStr
    password: str
    photo: Optional[str] = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Engelbert Tovar",
                "email": "admin@mail.dev",
                "password": "secretos",
                "photo": "https://images.pexels.com/photos/4804267/pexels-photo-4804267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        }

    class Settings:
        name = "admin"


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {"username": "admin@mail.dev", "password": "secreto"}
        }


class AdminData(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "Engelbert Tovar",
                "email": "admin@mail.dev",
            }
        }

# class UpdateAdminModel(BaseModel):
#     email: Optional[EmailStr]
#     password: Optional[str]
#     photo: Optional[str]
#     updated_at: Optional[datetime]

#     class Collection:
#         name = "admin"

#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "abdul@school.com",
#                 "photo": "https://images.pexels.com/photos/4804267/pexels-photo-4804267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
#                 "updated_at": datetime.now(),
#             }
#         }
        
# class UpdateUserPassword(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str
    updated_at: Optional[datetime]
    class Config:
        schema_extra = {
            "example": {
                "current_password": "secret1",
                "new_password": "secret2",
                "confirm_password": "secret2",
                "updated_at": datetime.now(),
            }
        } 
        

    