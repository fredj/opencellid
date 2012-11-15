from bottle import get, abort, request
import sqlsoup

db = sqlsoup.SQLSoup('sqlite:///cells.sqlite')


@get('/')
def get():
    criterion = {
        'mcc': request.query.get('mcc'),
        'mnc': request.query.get('mnc'),
        'lac': request.query.get('lac'),
        'cellid': request.query.get('cellid'),
        }
    cell = db.cell.filter_by(**criterion).first()
    if cell:
        return {'lon': cell.lon, 'lat': cell.lat, 'range': cell.range}
    else:
        abort(404)
