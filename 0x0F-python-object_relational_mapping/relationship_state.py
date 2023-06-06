#!/usr/bin/python3
""" a python file that contains the class definition of a State and an instance
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship


my_meta = MetaData()
Base = declarative_base(metadata=my_meta)


class State(Base):
    """
    State class inherits from Base links to the MySQL table states"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
