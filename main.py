from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import Crud, Model, Schemas
from database import local_session, db_engine
from fastapi.middleware.cors import CORSMiddleware

Model.Base.metadata.create_all(bind=db_engine)

app = FastAPI()

origins = [
    "https://desolate-sea-33600.herokuapp.com/users/first",
    "https://desolate-sea-33600.herokuapp.com/",
    "https://desolate-sea-33600.herokuapp.com/users",
    "https://frontpagereact.pages.dev/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=Schemas.author)
def create_user(user: Schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = Crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return Crud.create_user(db=db, user=user)


@app.get("/users/", response_model=Schemas.author)
def read_users(skip: int, limit: int, db: Session = Depends(get_db)):
    users = Crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=Schemas.author)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = Crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user
