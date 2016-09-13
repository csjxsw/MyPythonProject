#!/usr/bin/env python
# coding=utf-8

array = [1, 2, 5, 3, 6, 8, 4]

for i in range(len(array)-1, 0, -1):
    for j in range(0, i):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
print array

s1 = (2, 1.3, 'love', 5.6, 9, 12, False)
s2 = [True, 5, 'smile']
s2.append(343242.234)
for a in s2:
    print a

s3 = [1, [3, 4, 5]]
print s1, type(s1)
print s2, type(s2)
print s3, type(s3)


