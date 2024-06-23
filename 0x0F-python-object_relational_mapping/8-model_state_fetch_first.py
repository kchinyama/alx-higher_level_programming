#!/usr/bin/python3


"""demo script diplaying first state in table
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':

    myEngine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

    Base.metadata.create_all(myEngine)

    Session = sessionmaker(bind=myEngine)

    mySession = Session()

    myState = mySession.query(State).filter(State.name == 'California').first()

    if not myState:
        print('Nothing')

    else:
        print(f'{myState.id}: {myState.name}')

    mySession.close()
