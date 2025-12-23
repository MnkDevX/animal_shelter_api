from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.security import hash_password, verify_password

def create_user(db: Session, username, password):
    user = User(
        username=username,
        password_hash=hash_password(password)
    )
    db.add(user)
    db.commit()
    return user

def authenticate_user(db: Session, username, password):
    user = db.query(User).filter_by(username=username).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user
