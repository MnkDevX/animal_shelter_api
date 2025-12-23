from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core.database import SessionLocal
from app.auth.auth_service import create_user, authenticate_user
from app.auth.security import create_access_token
from app.schemas.user import UserCreate, Token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.password)

@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form.username, form.password)
    if not user:
        raise HTTPException(401, "Invalid credentials")

    token = create_access_token(
        {"sub": user.username, "role": user.role},
        ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {"access_token": token}
