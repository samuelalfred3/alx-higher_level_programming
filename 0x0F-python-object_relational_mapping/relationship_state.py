#!/usr/bin/python3
"""Defines the State class."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base

class State(Base):
    """Represents a state for a MySQL database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

