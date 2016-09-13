#!/usr/bin/python

import psycopg2
import re 

conn = psycopg2.connect(database="dataService", user="cloud", password="cloud", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

company = [(15, 'Jake', 35, 'shanghai', 40000.00),
           (16, 'Jones', 45, 'beijing', 50000.00),
           (17, 'Tom', 55, 'chengdu', 60000.00),
           (18, 'Lily', 25, 'taiyuan', 70000.00)
           ]

cur.executemany("""INSERT INTO dataservice.COMPANY VALUES (%s, %s,%s, %s,%s)""", company)
'''
company = [(5, 'Jake', 35, 'shanghai', 40000.00),
           (6, 'Jones', 45, 'beijing', 50000.00),
           (7, 'Tom', 55, 'chengdu', 60000.00),
           (8, 'Lily', 25, 'taiyuan', 70000.00)
           ]

cur.execute("INSERT INTO dataservice.COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'Jake', 35, 'shanghai', 40000.00)")
cur.execute("INSERT INTO dataservice.COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES (6, 'Jones', 45, 'beijing', 50000.00)")
cur.execute("INSERT INTO dataservice.COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES (7, 'Tom', 55, 'chengdu', 60000.00)")
cur.execute("INSERT INTO dataservice.COMPANY(ID,NAME,AGE,ADDRESS,SALARY) VALUES (8, 'Lily', 25, 'taiyuan', 70000.00)")
'''
conn.commit()
print "Records created successfully"
conn.close()
