#!/usr/bin/env python
#coding = utf-8

import psycopg2
import csv
import time

startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

conn = psycopg2.connect(database="dataService", user="cloud", password="cloud", host="10.254.201.218", port="5432")
print "Opened database successfully"

cur = conn.cursor()
csvfile = file('C:\\data\\201611mr-bj.csv', 'rb')
reader = csv.reader(csvfile)
count = 0
data = []
titleNUm = 0

for line in reader:
    count = count + 1
    if line:
        print count, ":", line
        if count == 1:
            tempStr = ','.join(line).decode('gbk')
            titleNUm = tempStr.split(',').__len__()
            print "titleNUm=", titleNUm
        if count > 1:
            tempStr = ','.join(line).decode('gbk')
            #print "str=", tempStr
            tempList = []
            tempStrArray = tempStr.split(',')
            tempLen = tempStrArray.__len__()
            if tempLen == titleNUm:
                for d in tempStrArray:
                    if d == "" or d is None:
                        tempList.append(0)
                    else:
                        tempList.append(d)
                data.append(tempList)
            else:
                print "tempLen=", tempLen
        if count % 200 == 0:
            #print "data=\n", data
            cur.executemany("""INSERT INTO kpihourbyscenario(dt,province,city,earfcn,covertype,scenario,vendor,num,eu0317,eu0113,eu0202,eu0104,eu0538,eu0103,eu0226,eu0306,eu0505,eu0506) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",data)
            conn.commit()
            #print "Records created successfully"
            data = []
    else:
        break

if data.__len__() > 1:
    print "data.size()=", data.__len__()
    cur.executemany(
          """INSERT INTO kpihourbyscenario(dt,province,city,earfcn,covertype,scenario,vendor,num,eu0317,eu0113,eu0202,eu0104,eu0538,eu0103,eu0226,eu0306,eu0505,eu0506) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        data)
    conn.commit()
    print "Records created successfully"
    print "data=\n", data
    data = []

csvfile.close()
conn.close()

endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "startTime:", startTime
print "endTime:", endTime
print "--------end-----------"