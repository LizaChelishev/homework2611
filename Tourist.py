from db_config import Base
from sqlalchemy import Column, Integer,  String, ForeignKey


class Tourist(Base):
    __tablename__ = 'tourist'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String())
    origin_country = Column(String())
