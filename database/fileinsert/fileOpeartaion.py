#!/usr/bin/env python
#coding=utf-8
import codecs
import time
import csv

# 格式化成2016-03-20 11:45:39形式
startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

csvfile = file('C:\\data\\201611mr-cq.csv', "rb")
reader = csv.reader(csvfile)
for line in reader:
    print line
csvfile.close()

endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "开始时间：", startTime
print "结束时间：", endTime
print "--------end-----------"