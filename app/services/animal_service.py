from sqlalchemy.orm import Session
from app.models.animal import Animal

def create_animal(db: Session, data):
    animal = Animal(**data.dict())
    db.add(animal)
    db.commit()
    db.refresh(animal)
    return animal

def get_animals(db: Session):
    return db.query(Animal).all()
