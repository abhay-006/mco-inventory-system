# ORM model representing the gun table
from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Gun(Base):
    __tablename__ = "gun"

    gun_id = Column(Integer, primary_key=True)
    gun_model = Column(String)
    gun_type = Column(String)
    repair_level = Column(String)
    annual_target = Column(Integer)
