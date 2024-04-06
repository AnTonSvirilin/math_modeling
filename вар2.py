import matplotlib.pyplot as plt
from numpy import *
a=2.7
x1=0.62
def ff(x):
        return a*x*(1-x)
b=a*x1*(1-x1)/x1
def fl(x):
        return b*x
x=0.1
y=0
Y=[]
X=[]
for i in arange(1,30,1):
        X.append(x)
        Y.append(y)
        y=ff(x)
        X.append(x)
        Y.append(y)
        x=y/b
plt.title('Паутинная диаграмма логистической \n функции λx(1-x) при λ = 2.7')
plt.plot(X,Y,'r')
x1=arange(0,1,0.001)
y1=[ff(x) for x in x1]
y2=[fl(x) for x in x1]
plt.plot(x1,y1,'b')
plt.plot(x1,y2,'g')

plt.savefig('ugduwike.png')