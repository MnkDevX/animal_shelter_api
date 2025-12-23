from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    age = Column(Integer)
    vaccinated = Column(Boolean, default=False)
    adopted = Column(Boolean, default=False)
