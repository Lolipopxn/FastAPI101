from pydantic import BaseModel
#Step 3: Pydantic Model

#1 - Base
class ItemBase(BaseModel):
    title: str
    description: str
    price: float

#2 - Request
class ItemCreated(ItemBase):
    pass

#3 - Response
class ItemResponse(ItemBase):
    id: int
    class Config:
        from_attributes = True