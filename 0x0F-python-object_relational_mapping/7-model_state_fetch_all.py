#!/usr/bin/python3
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engin = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engin)
    session = Session()

    stat = session.query(State).order_by(State.id).all()

    for i in stat:
        print("{}: {}".format(i.id, i.name))

    session.close()
