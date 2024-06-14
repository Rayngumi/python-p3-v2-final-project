# lib/models/patron.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Patron(Base):
    __tablename__ = 'patrons'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_year = Column(Integer)
    sobriety = Column(String)
    dress_code = Column(String)
    event_id = Column(Integer, ForeignKey('events.id'))
    
    event = relationship("Event", back_populates="patrons")

    def __init__(self, name, birth_year, sobriety, dress_code, event_id):
        self.name = name
        self.birth_year = birth_year
        self.sobriety = sobriety
        self.dress_code = dress_code
        self.event_id = event_id

    def __repr__(self):
        return f"<Patron(name={self.name}, birth_year={self.birth_year}, sobriety={self.sobriety}, dress_code={self.dress_code})>"
