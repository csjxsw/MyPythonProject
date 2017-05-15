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
BayesNet=[0.814,0.814,0.814,0.910,0.917,0.916,0.916,0.916,0.915,0.904,0.902];
C45=[0.814,0.814,0.883,0.917,0.922,0.921,0.926,0.925,0.927,0.926,0.925];
Logic=[0.814,0.815,0.814,0.852,0.904,0.904,0.905,0.905,0.905,0.908,0.908];
SMO=[0.814,0.814,0.814,0.814,0.890,0.890,0.891,0.894,0.895,0.897,0.897];
AdaboostM1=[0.814,0.814,0.885,0.917,0.908,0.908,0.908,0.908,0.908,0.911,0.912];
RadomForest=[0.872,0.890,0.901,0.910,0.914,0.912,0.913,0.914,0.914,0.920,0.916];


BayesNet, = plt.plot(x,BayesNet,'bo-')#,xx,yy,'r-',xx,yy,'bs'
C45, = plt.plot(x,C45,'rs-')
Logic, = plt.plot(x,Logic,'g*-')
SMO, = plt.plot(x,SMO,'cx-')
AdaboostM1, = plt.plot(x,AdaboostM1,'m>-')
RadomForest, = plt.plot(x,RadomForest,'y^-')

plt.title(u"F1值/属性数量")
plt.legend([BayesNet,C45,Logic,SMO,AdaboostM1,RadomForest],('BayesNet','C45','Logic','SMO','AdaboostM1','RadomForest'),'best', numpoints=1);
plt.grid(True)
plt.ylabel(u"F1值")
plt.xlabel(u"属性数量")
plt.axis([1,12,0.75,1])
#plt.xticks(range(min(y),max(y)))
plt.show()

