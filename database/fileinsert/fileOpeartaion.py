# coding=utf-8
import codecs

f = codecs.open('C:\\data\\201611mr-cq.csv', 'rb', 'utf-8')
s = f.readlines()
f.close()
for line in s:
    print line.encode('utf-8')