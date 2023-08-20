#!/usr/bin/python3
"""
Creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Accesses the database and get the states
    from the database hbtn_0e_100_usa
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
