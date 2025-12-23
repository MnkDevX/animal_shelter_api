from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Adoption(Base):
    __tablename__ = "adoptions"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    adopter_name = Column(String)
