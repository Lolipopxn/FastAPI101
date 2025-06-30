from sqlalchemy import Column, Integer, String, Float
from .database import Base

#step 2: ORM class
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)