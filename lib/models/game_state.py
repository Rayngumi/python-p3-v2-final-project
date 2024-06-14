from sqlalchemy import Column, Integer
from . import Base

class GameState(Base):
    __tablename__ = 'game_state'
    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Integer, default=0)
    shift = Column(Integer, default=1)
