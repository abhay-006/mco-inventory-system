# ORM model for transactions
from sqlalchemy import Column, Integer, ForeignKey, String
from app.database.base import Base

class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    inventory_id = Column(Integer, ForeignKey("inventory.id"))
    action = Column(String)
