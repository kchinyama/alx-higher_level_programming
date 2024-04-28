#!/usr/bin/python3


"""demo of output of the first item on the list
"""


from model_state import State, Base
from sqlalchemy.orm import Session
from sys import argv
from sqlalchemy import create_engine


dbConnect = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

# create engine to connect to database
engine = create_engine(dbConnect)


with Session(engine) as outcome:
    result = outcome.query(State).first()

if result:
    print(f"{result.id}: {result.name}")

else:
    pass
