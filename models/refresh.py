from typing import Optional, Any
from beanie import Document
from datetime import datetime
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr

class Refresh(Document):
    email: EmailStr
    refresh_token: str


    class Config:
        schema_extra = {
            "example": {
                "email": "admin@mail.dev",
                 "refresh_token": "rwerw4535wre5345t4trehgryu753",

            }
        }

    class Settings:
        name = "refresh_jwt"


class RefreshToken(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {"email": "admin@mail.dev", "refresh_token": "rwerw4535wre5345t4trehgryu753"}
        }


class RefreshData(BaseModel):
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "email": "admin@mail.dev",
                "refresh_token": "rwerw4535wre5345t4trehgryu753"
            }
        }
        
class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }
