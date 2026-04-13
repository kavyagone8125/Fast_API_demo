"""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#ORM = Object relational Mapping used to connect and avoids you to write SQL query
#ex without ORM
#INSERT INTO STUDENT(NAME,ABE) VALUES()
#By using the orm IT IS EASY
#STUDENT = student(name=" ",age=" ")
from config import DB_USER, DB_PASSWORD,DB_HOST,DB_NAME

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
