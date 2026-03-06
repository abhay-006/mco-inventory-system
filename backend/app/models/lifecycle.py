# ORM model for lifecycle tracking
from sqlalchemy import Column, Integer, ForeignKey, String
from app.database.base import Base

class Lifecycle(Base):
    __tablename__ = "lifecycle"
    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey("transaction.id"))
    status = Column(String)
