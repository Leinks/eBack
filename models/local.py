from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel, EmailStr

class Local(Document):
    name: str
    document:str
    phone: Optional[str] = None
    email: EmailStr
    logo: Optional[str] = None
    description:str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Facebook",
                "document": "J-334442234",
                "phone": "+584145555",
                "email": "facebook@mail.com",
                "logo": "https//logo.com",
                "description": "Somos La Mejor Red Social Ven y Conectate !",
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        }

    class Settings:
        name = "locals"


class UpdateLocalModel(BaseModel):
    name: Optional[str]
    document:Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    logo: Optional[str]
    description:Optional[str]
    updated_at: Optional[datetime]

    class Collection:
        name = "locals"

    class Config:
        schema_extra = {
            "example": {
                "name": "Facebook",
                "document": "J-334442234",
                "phone": "+584145555",
                "email": "facebook@mail.com",
                "logo": "https//logo.com",
                "description": "Somos La Mejor Red Social Ven y Conectate !",
                "updated_at": datetime.now(),
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
