from bottle import Bottle, abort, request
from bottle.ext.sqlalchemy import SQLAlchemyPlugin
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table

Base = declarative_base()
engine = create_engine('sqlite:///cells.sqlite')

class Cell(Base):
    __table__ = Table('cell', Base.metadata, autoload=True, autoload_with=engine)

    @property
    def json(self):
        return {'lon': self.lon, 'lat': self.lat, 'range': self.range}

app = Bottle()
app.install(SQLAlchemyPlugin(engine))

@app.get('/')
def get(db):
    criterion = {
        'mcc': request.query.get('mcc'),
        'mnc': request.query.get('mnc'),
        'lac': request.query.get('lac'),
        'cellid': request.query.get('cellid'),
        }
    cell = db.query(Cell).filter_by(**criterion).first()
    return cell.json if cell else abort(404)
