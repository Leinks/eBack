from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel

class Category(Document):
    name: str
    photo: Optional[str] = None
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "name": "Hamburguesas",
                "photo": "https//photo.com",
            }
        }

    class Settings:
        name = "categories"


class UpdateCategoryModel(BaseModel):
    name: str
    photo: Optional[str] = None
    updated_at: Optional[datetime] = datetime.now()

    class Collection:
        name = "categories"

    class Config:
        schema_extra = {
            "example": {
                "name": "Hamburguesas",
                "photo": "https//photo.com",
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
                "data": "Category Success !",
            }
        }
