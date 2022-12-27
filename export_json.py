import psycopg2
import json

username = 'postgres'
password = '****'
database = 'channels'
host = 'localhost'
port = '5432'


OUTPUT_FILE = 'all_data.json'

TABLES = [
    'channel',
    'genre',
    'country',
    'viewss'
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
    cur = conn.cursor()

    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open(OUTPUT_FILE, 'w') as outf:
    json.dump(data, outf, default=str, indent=4)
