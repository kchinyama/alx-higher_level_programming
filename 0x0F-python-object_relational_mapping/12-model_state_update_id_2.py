#!/usr/bin/python3


"""demo script to change a record inside a table
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy import update


if __name__ == '__main__':

    myEngine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    Base.metadata.create_all(myEngine)

    Session = sessionmaker(bind=myEngine)

    mySession = Session()

    editState = update(State).values(name='New Mexico').where(State.id==2)
    
    mySession.execute(editState)

    mySession.commit()

    mySession.close()
