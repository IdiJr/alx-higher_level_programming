#!/usr/bin/python3
"""
Defines the State class and creates the Base instance using SQLAlchemy.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class that represents a state in the database.
    Attributes:
        __tablename__(str): Table name of the class
        id (int): State id of the class
        name (str): State name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
