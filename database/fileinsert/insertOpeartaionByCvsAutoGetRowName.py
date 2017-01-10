#!/usr/bin/env python
#coding = utf-8
import sys,os
import psycopg2
import csv
import time

def genNums(num):
    str = ''
    count = 0
    while count < num:
        str = str + '%s,'
        count = count+1
    str = str[:-1]
    return str

startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
basepath = sys.path[0]
tablename = ''
titleStr = ''
title_s = ''
insertsql = ''

for param in sys.argv:
    if param.find('py') >= 0:
        continue

    path = basepath + os.sep + param
    tablename = param.replace(".csv", "")

    conn = psycopg2.connect(database="dataService", user="cloud", password="cloud", host="10.254.201.218", port="5432")
    print "Opened database successfully"

    cur = conn.cursor()
    csvfile = file(path, 'rb')#'C:\\data\\kpidaybyscenario.csv'
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
                titleStr = tempStr
                titleNUm = tempStr.split(',').__len__()
                print "titleNUm=", titleNUm
                title_s = genNums(titleNUm)
                insertsql = 'INSERT INTO '+tablename+'('+titleStr+')'+' VALUES ('+title_s+')'
                print "insertsql=",insertsql
            if count > 1:
                tempStr = ','.join(line).decode('gbk')
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
            if count % 1000 == 0:
                #print "data=\n", data
                cur.executemany(insertsql,data)
                conn.commit()
                #print "Records created successfully"
                data = []
        else:
            break

    if data.__len__() > 0:
        print "data.size()=", data.__len__()
        cur.executemany(insertsql,data)
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
