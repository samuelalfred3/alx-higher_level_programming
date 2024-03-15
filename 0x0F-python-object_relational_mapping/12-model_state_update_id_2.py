#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def update_state(engine, state_id, new_name):
    """Update the name of a State with given id"""
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=state_id).first()

    if state:
        state.name = new_name
        session.commit()
        print("State name updated successfully")
    else:
        print("State with id {} not found".format(state_id))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    update_state(engine, 2, "New Mexico")

