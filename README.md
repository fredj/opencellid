# opencellid

An [OpenCellID](http://www.opencellid.org/) HTTP server using [Bottle](http://bottlepy.org/).

## Install
Download and create an sqlite database from the csv data:

    curl http://dump.opencellid.org/cellsIdData/cells.txt.gz | gunzip - > cells.txt
    cat schema.sql | sqlite3 cells.sqlite
    cat import.sql | sqlite3 cells.sqlite

Create the virtual environemnt

    virtualenv .
    . bin/activate
    pip install -r requirements.txt

## Running
Start the server

    bottle.py opencellid:app

See `bottle.py --help` for more options (port, server, ...).

## Query

    curl -s 'http://localhost:8080/?mcc=228&mnc=1&lac=505&cellid=10545' | python -mjson.tool

The outout is a JSON string containing the latitude, longitude and the range (accuracy radius in meters)

## License
Copyright (c) 2012 Frédéric Junod <frederic.junod@gmail.com>

Released under the [WTFPL version 2](http://sam.zoy.org/wtfpl/).
