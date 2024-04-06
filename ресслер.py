import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#Создаем функцию правой части системы уравнений.
a,b,c=0.398,2.0,4.0
def f(y, t):
 y1, y2, y3 = y
 return [(-y2-y3),
 y1+a*y2,
 b+y3*(y1-c)]
#Решаем систему ОДУ и строим ее фазовую траекторию
t = np.linspace(0,50,5001)
y0 = [0, 0, 0]
[y1,y2,y3]=odeint(f, y0, t, full_output=False).T

fig = plt.figure(facecolor='white') 
ax = fig.add_subplot(111, projection='3d')
ax.plot(y1,y2,y3)
plt.xlabel('y1')
plt.ylabel('y2')
plt.title("Начальные условия: y0 = [0, 0, 0]")
plt.savefig('kfk.png')