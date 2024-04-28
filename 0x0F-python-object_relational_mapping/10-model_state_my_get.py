#!/usr/bin/python3

"""demo script that prints all items in a table
"""



from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':

    db = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # create engine to connect to database
    engine = create_engine(db)

    # create session to interact with tables
    Session = sessionmaker(bind=engine)

    session = Session()

    # query the database for the data
    request = session.query(State)

    if argv[4] in request:
        print(f"{argv[4]}")

    else:
        print("Not found")
