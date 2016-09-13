#!/usr/bin/env python
# coding=utf-8

def test_func():
    try:
        m = 1/0
    except NameError:
        print("Catch NameError in the sub-function")

try:
    test_func()
except ZeroDivisionError:
    print("Catch error in the main program")


def f(x):
    x = 100
    print x
a = 1
f(a)
print a

def f(x):
    x[0] = 100
    print x

a = [1,2,3]
f(a)
print a

xl = [1,3,5]
yl = [9,12,13]
L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]

a="abc"
b="efg"
c=a+b
print(c)

class SampleMore(object):
    def __call__(self, a):
        return a + 5

add = SampleMore()     # A function object
print(add(2))          # Call function
map(add, [2, 4, 5])    # Pass around function object
print(map)

