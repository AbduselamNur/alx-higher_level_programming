#!/usr/bin/python3
"""
 a script that lists all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4]

    stat = session.query(State).filter(state_name == State.name).first()
    if stat:
        print("{}".format(stat.id))
    else:
        print("Not found")

    session.close()
