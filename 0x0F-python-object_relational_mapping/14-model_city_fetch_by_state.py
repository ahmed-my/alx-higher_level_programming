#!/usr/bin/python3
"""script that deletes all State object with a name containing the
   letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = session.query(State.name, City.id,
                               City.name).filter(State.id == City.state_id)
    for state in state_name:
        print(state[0] + ": (" + str(state[1]) + ") " + state[2])
