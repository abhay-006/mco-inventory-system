# Pydantic schema for inventory items
from pydantic import BaseModel

class InventorySchema(BaseModel):
    component_id: int
    quantity: int
