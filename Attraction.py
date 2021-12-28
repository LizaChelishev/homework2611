from db_config import Base
from sqlalchemy import Column, Integer,  String, ForeignKey


class Attraction(Base):
    __tablename__ = 'attraction'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String())
    price = Column(Integer())
