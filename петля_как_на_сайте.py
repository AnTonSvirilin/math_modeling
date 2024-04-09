import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})




#Создаем функцию правой части системы уравнений.
s,r,b=10,25,3
def f(y, t):
 y1, y2, y3 = y
 return [s*(y2-y1),
 -y2+(r-y3)*y1,
-b*y3+y1*y2]
#Решаем систему ОДУ и строим ее фазовую траекторию
t = np.linspace(0, 20,2001)
y0 = [1, -1, 10]
[y1,y2,y3]=odeint(f, y0, t, full_output=False).T
	
ball, = ax.plot(y1, y2, y3, 'o', color='b') # Сферический объект
line, = ax.plot(y1, y2, y3, '-', color='b') # Линия
 
# Функция подстановки координат в анимируемые объекты
def animate(i):
    ball.set_data([y1[i]], [y2[i]])
    ball.set_3d_properties(y3[i])
 
    line.set_data(y1[:i], y2[:i])
    line.set_3d_properties(y3[:i])
 
ax.plot(y1,y2,y3)
plt.xlabel('y1')
plt.ylabel('y2')
plt.title("Начальные условия: y0 = [1.0001, -1, 10]")

ani = FuncAnimation(fig, animate, 100, interval=50)
 
ani.save('3D_motion.gif')