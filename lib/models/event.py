from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    patrons = relationship("Patron", back_populates="event")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Event(name={self.name})>"
