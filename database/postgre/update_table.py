#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="dataService", user="cloud", password="cloud", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("UPDATE dataservice.COMPANY set SALARY = 20000.00 where ID=1")
conn.commit
#conn.commit
print "Total number of rows updated :", cur.rowcount

cur.execute("SELECT id, name, address, salary  from dataservice.COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";
conn.commit()
conn.close()  
