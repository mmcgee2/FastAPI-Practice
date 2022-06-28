from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.environ.get("DATABASE_URL")

db_engine = create_engine(DATABASE_URL, pool_pre_ping = True)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()
