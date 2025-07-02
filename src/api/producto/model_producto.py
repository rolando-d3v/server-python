from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str]
    stock: int
    estado_activo: bool
