import email

from fastapi import FastAPI, Depends, Header 
from database import SessionLocal, Base, engine
from models import Users, Categories, Tasks
from schemas import Register, Login, CategoryCreate, TaskCreate
from auth import verify_token, create_token, hash_password, verify_password

Base.metadata.create_all(bind=engine)

app = FastAPI() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def current_user (token: str):
    return verify_token(token)["user_id"]

@app.post("/register")
def register(data:Register , db = Depends(get_db)):
    user = Users(email=data.email, password = hash_password(data.password))
    db.add(user)
    db.commit()
    return {
        "message": "User registered successfully",
        "user_id": user.id
    }
    