from pydantic import BaseModel

class Register(BaseModel):
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class CategoryCreate(BaseModel):
    name: str 

class TaskCreate(BaseModel):
    title: str
    category_id: int