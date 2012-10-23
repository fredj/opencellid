from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table

Base = declarative_base()

class Cell(Base):
    __table__ = Table('cell', Base.metadata, autoload=True)
