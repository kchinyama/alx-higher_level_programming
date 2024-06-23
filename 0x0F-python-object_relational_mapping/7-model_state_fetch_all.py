#!/usr/bin/python3


"""sqlalchemy demo of select/querying contents of a table
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':

    myEngine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                                            argv[2],
                                                                            argv[3]))

    Session = sessionmaker(bind=myEngine)

    Base.metadata.create_all(myEngine)

    mySession = Session()

    allStates = mySession.query(State).order_by(State.id).all()

    for state in allStates:
        print(f"{state.id}: {state.name}")

    mySession.close()
