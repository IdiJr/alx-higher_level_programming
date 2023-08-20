#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Accesses the database and get the states
    from the database hbtn_0e_14_usa
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State)
    for city, state in cities.all():
        print('{}: ({:d}) {}'.format(state.name, city.id, city.name))
    session.commit()
    session.close()
