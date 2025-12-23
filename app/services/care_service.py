from sqlalchemy.orm import Session
from app.models.care import Care

def create_care(db: Session, data):
    care = Care(**data.dict())
    db.add(care)
    db.commit()
    db.refresh(care)
    return care

def get_care(db: Session):
    return db.query(Care).all()
