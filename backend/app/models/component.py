# ORM model for components
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class Component(Base):
    __tablename__ = "component"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    assembly_id = Column(Integer, ForeignKey("assembly.id"))
