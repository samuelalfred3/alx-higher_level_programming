#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def create_objects(engine):
    """Creates State and City objects"""
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")

    san_francisco = City(name="San Francisco")

    california.cities.append(san_francisco)

    session.add(california)

    session.commit()

    session.close()

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

    Base.metadata.create_all(engine)

    create_objects(engine)

