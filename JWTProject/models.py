from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base
from sqlalchemy import DateTime
from datetime import datetime

class Users(Base):
    __tablename__ = "users" 
    id  = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

class Categories(Base):
    __tablename__ = "categories"
    id  = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))

class Tasks(Base):
    __tablename__ = "tasks"
    id  = Column(Integer, primary_key=True)
    title= Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    completed = Column(Boolean, default=False)
