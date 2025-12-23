from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.adoption import AdoptionCreate, AdoptionOut
from app.services.adoption_service import create_adoption, get_adoptions
from app.dependencies import get_current_user

router = APIRouter(prefix="/adoptions", tags=["Adoptions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AdoptionOut)
def adopt(
    adoption: AdoptionCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_adoption(db, adoption)


@router.get("/", response_model=list[AdoptionOut])
def list_adoptions(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_adoptions(db)
