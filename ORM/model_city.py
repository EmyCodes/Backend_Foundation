#!/usr/bin/python3
"""Module that contains the class State"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


if __name__ == "__main__":
    class City(Base):
        __tablename__ = "cities"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(150), nullable=False)
        state_id = Column(Integer, ForeignKey("states.id"), nullable=False)