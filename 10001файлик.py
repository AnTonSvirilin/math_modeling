# Импортируем пакеты
#ВОТ ЭТУ ХРЕНЬ НАДО СДЕЛАТЬ РАБОЧЕЙ ЛЮБОЙ ЦЕНОЙ!!!!!!!!!!!!
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation


# Позиционные массивы
a,b,c=0.398,2.0,4.0
def f(k, t):
 x, y, z = k
 return [(-y-z),
 x+a*y,
 b+z*(x-c)]
#Решаем систему ОДУ и строим ее фазовую траекторию
t = np.linspace(0,50,5001)
y0 = [0, 0, 0]
[x,y,z]=odeint(f, y0, t, full_output=False).T


# Задаем набор данных для анимации
dataSet = np.array([x, y, z])  # Комбинируем наши позиционные координаты
numDataPoints = len(t)
def animate_func(num):
   ax.clear()  # Очищаем фигуру для обновления линии, точки,  
               # заголовка и осей  # Обновляем линию траектории (num+1 из-за индексации Python)
   ax.plot3D(dataSet[0, :num+1], dataSet[1, :num+1],
             dataSet[2, :num+1], c='blue')    # Обновляем локацию точки 
   ax.scatter(dataSet[0, num], dataSet[1, num], dataSet[2, num],
              c='blue', marker='o')    # Добавляем постоянную начальную точку
   ax.plot3D(dataSet[0, 0], dataSet[1, 0], dataSet[2, 0],    
              c='black', marker='o')    # Задаем пределы для осей
   ax.set_xlim3d([-10, 10])
   ax.set_ylim3d([-10, 10])
   ax.set_zlim3d([0, 10])

   # Добавляем метки
   ax.set_title('Trajectory \nTime = ' + str(np.round(t[num], decimals=2)) + ' sec')
   ax.set_xlabel('x')
   ax.set_ylabel('y')
   ax.set_zlabel('z')

   # Рисуем анимацию
fig = plt.figure()
ax = plt.axes(projection='3d')
line_ani = animation.FuncAnimation(fig, animate_func, interval=100,  
                                  frames=numDataPoints)

line_ani.save('animate_func1111111111111111111111111.gif')