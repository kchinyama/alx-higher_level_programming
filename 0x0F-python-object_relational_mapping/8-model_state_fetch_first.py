#!/usr/bin/python3


"""demo of output of the first item on the list
"""


from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine


if __name__ == '__main__':

    dbConnect = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # create engine to connect to database
    engine = create_engine(dbConnect)


    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    result = session.query(State).order_by(State.id).first()

    if result:
        print(f"{result.id}: {result.name}")

    else:
        pass
