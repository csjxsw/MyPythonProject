#!/usr/bin/env python
# coding=utf-8

def fib(n):
    if(n<=2):
        return 1
    return fib(n-1)+fib(n-2)

def fib1(n):
    if(n<=2):
        return 1
    a1=1
    a2=1
    for index in range(n-2):
        temp = a1
        a1=a2
        a2=a2+temp
    return a2


if __name__ == '__main__':
    print fib1(5)