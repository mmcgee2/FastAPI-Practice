from black import Mode
from sqlalchemy.orm import Session
import Model, Schemas


def get_user(db: Session, user_id: str):
    return db.query(Model.User).filter(Model.User.au_id == user_id).first()


def get_users(db: Session, skip: int, limit: int):
    return db.query(Model.User).offset(skip).limit(limit).all()


def get_user_by_name(db: Session, name: str):
    return db.query(Model.User).filter(Model.User.au_fname == name).first()


def create_user(db: Session, user: Schemas.UserCreate):
    db_user = Model.User(au_fname=user.au_fname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
