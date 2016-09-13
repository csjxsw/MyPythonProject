#!/usr/bin/env python
# coding = utf-8

f = open("E:\data\cgi.txt")
count = 0

content = f.readlines()
for c in content:
    print c

f = open("E:\data\cgi.txt")
while True:
    line = f.readline()
    count = count + 1
    if line:
        print count, ":", line
    else:
        break

f.close()
print "--------end-----------"