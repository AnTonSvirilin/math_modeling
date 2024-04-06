import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#Создаем функцию правой части системы уравнений.
s,r,b=10,25,3
def f(y, t):
 y1, y2, y3 = y
 return [s*(y2-y1),
 -y2+(r-y3)*y1,
-b*y3+y1*y2]
#Решаем систему ОДУ и строим ее фазовую траекторию
t = np.linspace(0,20,2001)
y0 = [1, -1, 10]
[y1,y2,y3]=odeint(f, y0, t, full_output=False).T

fig = plt.figure(facecolor='white') 
ax = fig.add_subplot(111, projection='3d')
ax.plot(y1,y2,y3)
plt.xlabel('y1')
plt.ylabel('y2')
plt.title("Начальные условия: y0 = [1.0001, -1, 10]")
plt.savefig('kfk2.png')