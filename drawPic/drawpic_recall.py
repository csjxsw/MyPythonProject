#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np

x=[]
y=[]
f=file('d:/precision.txt','r');
for line in f.readlines():
    temp=line.split(" ")
    x.append(int(temp[0]))
    y.append(float(temp[1].strip()))
f.close

xx=[]
yy=[]
f=file('d:/precision.txt','r');
for line in f.readlines():
    temp=line.split(" ")
    xx.append(int(temp[0]))
    yy.append(float(temp[1].strip()))
f.close

x=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10,11 ];
BayesNet=[0.873,0.873,0.873,0.923,0.926,0.925,0.925,0.924,0.921,0.908,0.904];
C45=[0.873,0.873,0.905,0.927,0.93,0.931,0.934,0.934,0.935,0.934,0.934];
Logic=[0.873,0.871,0.871,0.876,0.918,0.918,0.919,0.919,0.919,0.919,0.919];
SMO=[0.873,0.873,0.873,0.873,0.91,0.91,0.91,0.913,0.913,0.914,0.914];
AdaboostM1=[0.873,0.873,0.903,0.927,0.92,0.92,0.92,0.92,0.92,0.922,0.92];
RadomForest=[0.875,0.895,0.906,0.916,0.92,0.918,0.92,0.919,0.92,0.925,0.922];


BayesNet, = plt.plot(x,BayesNet,'bo-')#,xx,yy,'r-',xx,yy,'bs'
C45, = plt.plot(x,C45,'rs-')
Logic, = plt.plot(x,Logic,'g*-')
SMO, = plt.plot(x,SMO,'cx-')
AdaboostM1, = plt.plot(x,AdaboostM1,'m>-')
RadomForest, = plt.plot(x,RadomForest,'y^-')

plt.title(u"召回率/属性数量")
plt.legend([BayesNet,C45,Logic,SMO,AdaboostM1,RadomForest],('BayesNet','C45','Logic','SMO','AdaboostM1','RadomForest'),'best', numpoints=1);
plt.grid(True)
plt.ylabel(u"召回率")
plt.xlabel(u"属性数量")
plt.axis([1,12,0.8,1])
#plt.xticks(range(min(y),max(y)))
plt.show()

