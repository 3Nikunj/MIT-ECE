from typing import Optional
from pydantic import BaseModel

class ProductCreate (BaseModel) :
    name :str
    price :float
    description : Optional[str] = None 

class ProductUpdate (BaseModel) :
    name : Optional[str] = None
    price : Optional[float] = None
    description : Optional[str] = None
