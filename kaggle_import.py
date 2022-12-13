import csv
import decimal
import psycopg2
import psycopg2.extras
username = 'postgres'
password = '****'
database = 'channels'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'top50.csv'

query_1 = '''
INSERT INTO channel (ch_name, ch_views, ch_subscribers,id_genre, id_country) VALUES (%s, %s, %s, %s, %s)
'''
query_2 = '''
INSERT INTO country (id_country, country_name) VALUES (%s, %s)
'''

query_3 = '''
CREATE TABLE tab12 AS (SELECT ROW_NUMBER() OVER(ORDER BY country_name) AS id_country, country_name FROM country GROUP BY country_name )
'''

query_4 = '''
DROP TABLE tab12 
'''
query_5 = '''
DELETE FROM country 
'''

query_6 = '''
INSERT INTO country select id_country, country_name from tab12
'''

query_7 = '''
INSERT INTO genre (id_genre, genre_name) VALUES (%s, %s)
'''

query_8 = '''
CREATE TABLE newgenre AS (SELECT ROW_NUMBER() OVER(ORDER BY genre_name) AS id_genre, genre_name FROM genre GROUP BY genre_name)
'''

query_9 = '''
DROP TABLE newgenre 
'''
query_10 = '''
DELETE FROM genre 
'''

query_11 = '''
INSERT INTO genre select id_genre, genre_name from newgenre
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    cur4 = conn.cursor()
    cur5 = conn.cursor()

    cur6 = conn.cursor()
    cur7 = conn.cursor()

    #cur2.execute(query_5)
    #cur3.execute(query_4)

    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf, delimiter=',')
        for idx, row in enumerate(reader):
            id_country = idx + 1
            country_name = row['Country']

            values = (id_country, country_name)
            cur2.execute(query_2, values)

            cur3.execute(query_3)
            cur2.execute(query_5)
            cur2.execute(query_6)
            cur3.execute(query_4)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf, delimiter=',')
        for idx, row in enumerate(reader):
            id_genre = idx + 1
            genre_name = row['Channel Type']
            values3 = (id_genre, genre_name)
            cur6.execute(query_7, values3)
            cur7.execute(query_8)
            cur6.execute(query_10)
            cur6.execute(query_11)
            cur7.execute(query_9)

    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf, delimiter=',')
        for idx, row in enumerate(reader):
            ch_name = row['Channel']
            ch_views = row['Total Views(Till End Of The Week)']
            ch_subscribers = row['Number of Subscribers(In Millions)']

            id_genre = row['Channel Type']
            if not id_genre:
                continue
            cur5.execute('select id_genre from genre where genre_name = %s', (id_genre,))
            id_genre = cur5.fetchone()[0]

            id_country = row['Country']
            if not id_country:
                continue
            cur4.execute('select id_country from country where country_name = %s', (id_country,))
            id_country = cur4.fetchone()[0]

            name_c = row['Country']
            values2 = (ch_name, ch_views, ch_subscribers, id_genre, id_country)
            cur.execute(query_1, values2)


    conn.commit()
