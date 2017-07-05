# coding:utf-8
# !/usr/bin/env python

import regTrees
import matplotlib.pyplot as plt
from numpy import *

if __name__ == '__main__':
    myDat = regTrees.loadDataSet('data-train.csv')
    myMat = mat(myDat)
    print myMat.T
    Tree = regTrees.createTree(myMat)
    print Tree
    regTrees.plotBestFit('data-train.csv')