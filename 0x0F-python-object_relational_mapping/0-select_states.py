#!/usr/bin/python3
""" list to display all states from the database """
import MySQLdb
import sys

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    host = "localhost"
    db = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}/{db}",
                       pool_pre_ping=True)

    Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(256))


Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).all()
for state in states:
    print((state.id, state.name))

session.close()
