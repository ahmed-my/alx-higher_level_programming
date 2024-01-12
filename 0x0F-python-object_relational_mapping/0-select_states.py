#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


user = sys.argv[1]
passwd = sys.argv[2]
database = sys.argv[3]
host = "localhost"
port = 3306
if __name__ == "__main__":
    db = MySQLdb.connect(host, user, passwd, database, port)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

"""
import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

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

query_states = session.query(State).order_by(State.id).all()
for state in query_states:
    print((state.id, state.name))

session.close()
"""
