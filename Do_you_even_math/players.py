from sqlalchemy import Column, Integer, String
from connection import *


class Player(Base):

    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    points = Column(Integer)

    def __str__(self):
        return "{} with {} points.".format(self.name, self.points)

