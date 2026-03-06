# Pydantic schema for component data validation
from pydantic import BaseModel

class ComponentSchema(BaseModel):
    name: str
