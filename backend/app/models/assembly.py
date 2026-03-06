# ORM model for assemblies
from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Assembly(Base):
    __tablename__ = "assembly"
    id = Column(Integer, primary_key=True)
    name = Column(String)
