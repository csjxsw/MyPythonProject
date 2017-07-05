#!/usr/bin/env python
# coding = utf-8

'''

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

'''


all_the_text = "hello world"
file_object = open('thefile.txt', 'w')
file_object.write(all_the_text)
file_object.close()

print "--------end-----------"
