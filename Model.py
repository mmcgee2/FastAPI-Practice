from database import Base
from sqlalchemy import VARCHAR, Column, Integer, String

# from sqlalchemy.orm import relationship not yet as we only have 1 table for now in testing phase


class User(Base):
    __tablename__ = "authors"

    au_id = Column(String(11), primary_key=True, index=True)
    au_fname = Column(String(20), unique=True, index=True)
    phone = Column(String(12))
    age = Column(Integer)


"""
class User(Base):
    __tablename__ = "Viruses"

    species = Column(String(30), primary_key = True, index = True)
"""
