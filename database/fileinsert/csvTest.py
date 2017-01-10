#!/usr/bin/env python
# coding = utf-8

import csv

csvfile = file('C:\\data\\201611mr-cq.csv', "rb")
reader = csv.reader(csvfile)
for line in reader:
    print line
csvfile.close()
