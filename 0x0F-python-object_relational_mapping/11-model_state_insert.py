#!/usr/bin/python3
"""
Prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Accesses the database and get the states
    from the database hbtn_0e_6_usa
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    inserted_state = State(name="Louisiana")
    session.add(inserted_state)
    session.commit()
    print("{}".format(inserted_state.id))
    session.close()
