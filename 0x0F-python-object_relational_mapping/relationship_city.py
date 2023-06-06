#!/usr/bin/python3
"""
City Model"""
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """class inherits from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
