#!/usr/bin/env python
# coding=utf-8

dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
dic["jiangxin"] = 26
for key in dic:
    print key, dic[key]
print dic.keys()
print dic.values()
print dic.items()

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print (d['Michael'])


fruit = [234,234234,343.345,45.23]

#增，删，改，查

fruit.append(22.22)
print fruit
