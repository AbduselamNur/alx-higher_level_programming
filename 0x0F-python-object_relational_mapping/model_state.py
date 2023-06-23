#!/usr/bin/python3
""" a python file that contains the class definition of a State and an instance
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """
    State class inherits from Base links to the MySQL table states"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
