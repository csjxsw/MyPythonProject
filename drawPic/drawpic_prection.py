#-*-coding:utf-8-*-
import matplotlib.pyplot as plt

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
BayesNet=[0.763,0.763,0.763,0.921,0.923,0.921,0.921,0.918,0.915,0.902,0.901];
C45=[0.763,0.763,0.903,0.927,0.927,0.932,0.934,0.933,0.936,0.936,0.936];
Logic=[0.763,0.79,0.787,0.848,0.916,0.916,0.916,0.916,0.916,0.914,0.914];
SMO=[0.763,0.763,0.763,0.763,0.911,0.911,0.911,0.914,0.914,0.916,0.915];
AdaboostM1=[0.763,0.763,0.892,0.925,0.916,0.916,0.916,0.916,0.916,0.918,0.913];
RadomForest=[0.87,0.887,0.898,0.909,0.913,0.912,0.913,0.913,0.913,0.92,0.916];


BayesNet, = plt.plot(x,BayesNet,'bo-')#,xx,yy,'r-',xx,yy,'bs'
C45, = plt.plot(x,C45,'rs-')
Logic, = plt.plot(x,Logic,'g*-')
SMO, = plt.plot(x,SMO,'cx-')
AdaboostM1, = plt.plot(x,AdaboostM1,'m>-')
RadomForest, = plt.plot(x,RadomForest,'y^-')

plt.title(u"准确率/属性数量")
plt.legend([BayesNet,C45,Logic,SMO,AdaboostM1,RadomForest],('BayesNet','C45','Logic','SMO','AdaboostM1','RadomForest'),'best', numpoints=1);
plt.grid(True)
plt.ylabel(u"准确率")
plt.xlabel(u"属性数量")
plt.axis([1,12,0.7,1])
#plt.xticks(range(min(y),max(y)))
plt.show()

