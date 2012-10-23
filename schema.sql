CREATE TABLE cell (
    id INTEGER PRIMARY KEY,
    lat REAL,
    lon REAL,
    mcc INTEGER,
    mnc INTEGER,
    lac INTEGER,
    cellid INTEGER,
    range INTEGER,
    nbSamples INTEGER,
    created_at TEXT,
    updated_at TEXT,
    zero INTEGER
);
