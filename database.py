from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "mysql+pymysql://g7vn3rd05puohm91:odl20txpni2bpqo0@ebh2y8tqym512wqs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/nnrl2r877obkotl6"


db_engine = create_engine(DATABASE_URL, pool_pre_ping = True)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()
