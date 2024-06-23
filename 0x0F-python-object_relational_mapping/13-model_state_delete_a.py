#!/usr/bin/python3

"""demo script of delting records with a common character
"""



from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':

    myEngine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    Base.metadata.create_all(myEngine)

    Session = sessionmaker(bind=myEngine)

    mySession = Session()

    delStates = mySession.query(State).where(State.name.like('%a%')).all()

    for state in delStates:
        mySession.delete(state)

    mySession.commit()

    mySession.close()
