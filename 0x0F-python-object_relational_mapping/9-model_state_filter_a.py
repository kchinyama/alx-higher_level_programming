#!/usr/bin/python3


"""demo script showing the display of records with 'a'
"""



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':

    myEngine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    Base.metadata.create_all(myEngine)

    Session = sessionmaker(bind=myEngine)

    mySession = Session()

    myStates = mySession.query(State).filter(State.name.like('%a%')).all()

    for state in myStates:
        print(f"{state.id}: {state.name}")

    mySession.close()
