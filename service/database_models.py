from sqlalchemy import Column, Integer, String

from .database import Base


class Burial(Base):
    __tablename__ = "burials"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slots = Column(String)
    garden = Column(String)
    section = Column(String)
    lot = Column(String)
    block = Column(String)
    space = Column(String)