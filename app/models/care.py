from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Care(Base):
    __tablename__ = "care"

    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    description = Column(String)
