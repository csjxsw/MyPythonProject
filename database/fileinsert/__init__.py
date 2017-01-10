#!/usr/bin/env python
# coding = utf-8

import sys,os
from sys import argv

print sys.path[0]
print sys.argv
print os.sep

str = "this is string example....wow!!! this is really string"
replacestr = str.replace("is", "was")
print "replacestr=",replacestr

str = 'abcdefd'
substr = 'abc'
res = str.find(substr)
print "res=", res
if res >= 0:
    print "contains"
else:
    print "not contains"

i = 1
for param in sys.argv:
    path = sys.path[0]+os.sep+param
    print i, path
    i = i+1

print "--------end-----------"