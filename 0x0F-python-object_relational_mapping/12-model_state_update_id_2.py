#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
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

    update_state = session.query(State).filter(State.id == 2).first()
    update_state.name = "New Mexico"
    session.commit()
    session.close()
