from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.care import CareCreate, CareOut
from app.services.care_service import create_care, get_care
from app.dependencies import get_current_user

router = APIRouter(prefix="/care", tags=["Care"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CareOut)
def add_care(
    care: CareCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_care(db, care)


@router.get("/", response_model=list[CareOut])
def list_care(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_care(db)
