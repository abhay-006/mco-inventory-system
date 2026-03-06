# ORM model for inventory records
from sqlalchemy import Column, Integer, ForeignKey
from app.database.base import Base

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True)
    component_id = Column(Integer, ForeignKey("component.id"))
    quantity = Column(Integer)
