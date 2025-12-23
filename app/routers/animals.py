from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.animal import AnimalCreate, AnimalOut
from app.services.animal_service import create_animal, get_animals
from app.dependencies import get_current_user

router = APIRouter(prefix="/animals", tags=["Animals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AnimalOut)
def add_animal(
    animal: AnimalCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_animal(db, animal)

@router.get("/", response_model=list[AnimalOut])
def list_animals(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_animals(db)
