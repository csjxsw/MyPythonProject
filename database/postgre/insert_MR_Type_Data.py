#!/usr/bin/python
#coding=utf-8
import psycopg2
import re 

conn = psycopg2.connect(database="myGreenplum", user="test", password="test", host="172.16.140.131", port="5432")
print "Opened database successfully"

cur = conn.cursor()

data = [
(1,"高速公路","高速公路","scenario"),
(2,"高铁","高铁","scenario"),
(3,"高校","高校","scenario"),
(4,"地铁","地铁","scenario"),
(5,"核心城区","1","iscore"),
(6,"非核心城区","0","iscore"),
(7,"宏站","outdoor","covertype"),
(8,"室内","indoor","covertype"),
(9,"D频段","D","earfcn"),
(10,"E频段","E","earfcn"),
(11,"F频段","F","earfcn")
]
cur.executemany("""INSERT INTO mrscenariotype(id,name,value,type) VALUES (%s,%s,%s,%s)""", data)

conn.commit()
print "Records created successfully"
conn.close()
