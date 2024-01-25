from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel, EmailStr

class Company(Document):
    name: str
    document:str
    phone: Optional[str] = None
    email: EmailStr
    logo: Optional[str] = None
    description:str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "name": "Meta",
                "document": "J-366959589",
                "phone": "+584149999",
                "email": "meta@mail.com",
                "logo": "https//logo.com",
                "description": "Empresa dedicada a la Técnologia",
            }
        }

    class Settings:
        name = "companys"


class UpdateCompanyModel(BaseModel): 
    name: Optional[str] = None
    document:Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr]
    logo: Optional[str] = None
    description:Optional[str]
    updated_at: Optional[datetime] = datetime.now()

    class Collection:
        name = "companys"

    class Config:
        schema_extra = {
            "example": {
                "name": "Meta",
                "document": "J-366959589",
                "phone": "+584149999",
                "email": "meta@mail.com",
                "logo": "https//logo.com",
                "description": "Empresa dedicada a la Técnologia",
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
                "data": "Company success !",
            }
        }
