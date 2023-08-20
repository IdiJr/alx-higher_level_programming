#!/usr/bin/python3
"""
Defines the City class and creates the Base instance using SQLAlchemy.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class that represents a city in the database.
    Attributes:
        __tablename__(str): Table name of the class
        id (int): State id of the class
        name (str): State name of the class
        state_id (int): id of State in which the city belongs
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
