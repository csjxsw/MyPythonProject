#!/usr/bin/env python
# coding=utf-8


def genNums(num):
    str = ''
    count = 0
    while count < num:
        str = str + '%s,'
        count = count+1
    str = str[:-1]
    return str

if __name__ == '__main__':
    print ("------begin--------")
    reult = genNums(5)
    print reult
    print ("------end--------")

