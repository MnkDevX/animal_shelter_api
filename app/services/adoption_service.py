from sqlalchemy.orm import Session
from app.models.adoption import Adoption
from app.models.animal import Animal

def create_adoption(db: Session, data):
    animal = db.query(Animal).get(data.animal_id)
    animal.adopted = True

    adoption = Adoption(**data.dict())
    db.add(adoption)
    db.commit()
    db.refresh(adoption)
    return adoption

def get_adoptions(db: Session):
    return db.query(Adoption).all()
