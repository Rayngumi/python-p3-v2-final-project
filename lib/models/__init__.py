from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///game.db')
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    import models.patron
    import models.event
    import models.game_state
    Base.metadata.create_all(engine)
