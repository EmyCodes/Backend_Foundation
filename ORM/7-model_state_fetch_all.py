#!/usr/bin/python3
"""Module that contains the class State"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create Engine
    engine = create_engine(
        f"mysql+mysqldb:{argv[1]:argv[2]@localhost}/{argv[3]}")
    Session = sessionmaker()
    session = Session(bind=engine)

    states = session.query(State).order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))
