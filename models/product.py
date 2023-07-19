from typing import Optional, Any
from datetime import datetime
from beanie import Document
from pydantic import BaseModel

class Product(Document):
    name: str
    description:str
    price:int
    ref:int
    photo: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "name": "Hamburguesa La Reina",
                "description": "Hamburguesa Rellena de 100gr de Carne, Papas fritas, Huevo, Lechuga, Tomate Queso, Salsa de Tomate y Mayonesa",
                "price": "200",
                "ref": "6",
                "photo": "https//photo.com",
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
            }
        }

    class Settings:
        name = "products"


class UpdateProductModel(BaseModel):
    name: str
    description:str
    price:int
    ref:int
    photo: Optional[str] = None
    updated_at: Optional[datetime] = None

    class Collection:
        name = "products"

    class Config:
        schema_extra = {
            "example": {
                "name": "Hamburguesa La Reina",
                "description": "Hamburguesa Rellena de 100gr de Carne, Papas fritas, Huevo, Lechuga, Tomate Queso, Salsa de Tomate y Mayonesa",
                "price": "200",
                "ref": "6",
                "photo": "https//photo.com",
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
