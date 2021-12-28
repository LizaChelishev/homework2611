from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

connection_string = 'postgresql+psycopg2://postgres:liza1709liza@localhost/postgres'

Base = declarative_base()

Session = sessionmaker()
engine = create_engine(connection_string, echo=True)
local_session = Session(bind=engine)


def create_all_entities():
    Base.metadata.create_all(engine)
    return local_session
