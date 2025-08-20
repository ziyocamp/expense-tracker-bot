from sqlalchemy.orm import Session
from app.models.user import User


def get_or_create_user(db: Session, tg_id: int, full_name: str) -> User:
    """
    Returns a User by Telegram ID.  
    If not found, creates a new user and returns it.
    """
    user = db.query(User).filter_by(tg_id=tg_id).first()
    if user:
        return user

    user = User(tg_id=tg_id, full_name=full_name)
    db.add(user)
    db.flush()   # to get user.id immediately
    return user


def get_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        return user
