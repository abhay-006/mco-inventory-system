# ORM model for audit logs
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base

class Audit(Base):
    __tablename__ = "audit"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    action = Column(String)
