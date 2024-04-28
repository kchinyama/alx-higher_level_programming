#!/usr/bin/python3


"""demo script of the creation of a table and an instance
via the sqlalchemy module"""



import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import sys


"""create variable Base that hold declarative class attributes"""
Base = declarative_base()

class State(Base):
    """class State that inherits from the Base class"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

"""create engine variable that will connect with database at port 3306"""
#engine = create_engine('mysql://username:password@localhost:3306/database_name', echo=True)
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine, checkfirst=True)
