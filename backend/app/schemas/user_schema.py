# Pydantic schema for user operations
from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str
