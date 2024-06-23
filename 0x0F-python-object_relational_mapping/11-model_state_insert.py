#!/usr/bin/python3


"""demo script for adding new state to a table
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from sqlalchemy import func


if __name__ == '__main__':

    myEngine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")

    Base.metadata.create_all(myEngine)

    Session = sessionmaker(bind=myEngine)

    mySession = Session()

    addState = State(name='Louisiana')

    mySession.add(addState)

    mySession.commit()

    totalNum = mySession.query(func.count(State.id)).scalar()

    print(f"{totalNum}")

    mySession.close()
