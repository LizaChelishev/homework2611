from db_config import Base
from sqlalchemy import Column, Integer,  String, ForeignKey


class Visit(Base):
    __tablename__ = 'visit'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    tourist_id = Column(Integer(), ForeignKey('tourist.id'))
    attraction_id = Column(Integer(), ForeignKey('attraction.id'))
    year_of_visit = Column(Integer())
