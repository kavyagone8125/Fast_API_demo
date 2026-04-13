#Model.py is used to table creation
from sqlalchemy import Column, Integer, String
from database import engine
"""from sqlalchemy.orm import declarative_base  #create a declaration
Base = declarative_base()
class Student(Base):
    tablename = "students"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100))
    age = Column(Integer)
    course = Column(String(100))
#create table
Base.metadata.create_all(bind=engine)"""

from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)
    course = Column(String(100))
