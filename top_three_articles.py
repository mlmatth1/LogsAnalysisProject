#!/usr/bin/env python2.7

import psycopg2

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)

c = db.cursor()

c.execute("select * from view_top_three_articles")

results = c.fetchall()

for row in results:
    print '{0} {1} views'.format(row[0], row[1])

db.close()
