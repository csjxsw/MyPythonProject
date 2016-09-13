#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="dataService", user="cloud", password="cloud", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("DELETE from dataservice.COMPANY where ID=2;")
conn.commit
print "Total number of rows deleted :", cur.rowcount

cur.execute("SELECT id, name, address, salary  from dataservice.COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

conn.commit
print "Operation done successfully";
conn.close()  
