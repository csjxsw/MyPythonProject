#!/usr/bin/python
#coding=utf-8
import psycopg2
import re 

conn = psycopg2.connect(database="dataService", user="cloud", password="cloud", host="10.254.201.218", port="5432")
print "Opened database successfully"

cur = conn.cursor()

data = [
["20161101","CQ","155438-2","重庆","Huawei","38400","outdoor","普铁","长寿渝利铁路美化塔-HLH-2","24","14","107.0994503","29.8857074","0","840","72","34","6","0.9143","840","768","0.9143","0","0","5","5","155450-3:0.1084;155386-1:0.0972;155438-1:0.1286;155222-1:0.0459;155438-3:0.7222;","155450-3:0.1084;155386-1:0.0972;155438-1:0.1286;155222-1:0.0459;155438-3:0.7222;","0","0","0","0"],
["20161101","CQ","155372-3","重庆","Huawei","38400","outdoor","城区道路","长寿桃花老陈菜美化塔-HLH-3","28","11","107.0952447","29.858121","0","721","51","8","2","0.9293","721","670","0.9293","0.0373","0.0328","4","3","155376-1:0.1309;155392-2:0.0334;155372-1:0.0724;155366-2:0.0398;","155376-1:0.1309;155372-1:0.0724;155366-2:0.0398;","0","0","0","0"]
]

cur.executemany("""INSERT INTO networkstructure201611(dt,province,cgi,city,vendor,earfcn,covertype,scenario,chinesename,height,totaltilt,bdlng,bdlat,iscore,rtotal,rweak,rweak2,rweak3,rcoverage,ototal,ovalid,ocoverage,oover,osover,affect,saffect,affectlist,saffectlist,utotal,ugood,dtotal,dgood) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", data)



conn.commit()
print "Records created successfully"
conn.close()
