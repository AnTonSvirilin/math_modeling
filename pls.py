#делаюфайлик + петля 


import matplotlib.animation as animation
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
ax.plot3D(y1,y2,y3)
plt.xlabel('y1')
plt.ylabel('y2')
plt.title("Начальные условия: y0 = [1.0001, -1, 10]")
#plt.savefig('kfk2.png')


fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)
 
 
# Функция инициализации.
def init():
    # создение пустого графа.
    line.set_data([], [], [])
    return line,
 
 
xdata, ydata, zdata = [], [], []
 
 
# функция анимации
def animate(i):
    t = 0.1 * i
 
    # x, y данные на графике
    x = y1
    y = y2
    z = y3
    # добавление новых точек в список точек осей x, y
    xdata.append(x)
    ydata.append(y)
    zdata.append(z)
    line.set_data(xdata, ydata, zdata)
    return line,
 
 
# Вызов анимации.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=500, interval=20, blit=True)
 
# Сохраняем анимацию как gif файл
anim.save('coil.gif', writer='imagemagick')