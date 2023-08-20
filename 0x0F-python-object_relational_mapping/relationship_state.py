#!/usr/bin/python3
"""
Defines the State class and creates the Base instance using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City

Base = declarative_base()


class State(Base):
    """
    State class that represents a state in the database.
    Attributes:
        __tablename__(str): Table name of the class
        id (int): State id of the class
        name (str): State name of the class
        cities (:obj: `City`): Cities belonging to the state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
