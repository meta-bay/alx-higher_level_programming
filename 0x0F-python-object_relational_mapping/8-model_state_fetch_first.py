#!/usr/bin/python3
'''
    fetch first state
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = Session(engine)
    first_s = session.query(State).filter(State.id == 1).first()
    if first_s:
        print("{}: {}".format(first_s.id, first_s.name))
    else:
        print("Nothing")
    session.close()
