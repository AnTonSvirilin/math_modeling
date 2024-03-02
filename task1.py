import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 200
t = np.linspace(0, 5, frames)

# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    x, vx, y, vy = z
    
    dx_dt = vx
    dvx_dt = -F/m
    dy_dt = vy
    dvy_dt = - g + F/m
    
    return dx_dt, dvx_dt, dy_dt, dvy_dt

# Определяем начальные значения и параметры
g = 9.8
v = 20
alpha = 60 * np.pi / 180

x0 = 0
vx0 = v * np.cos(alpha)
y0 = 0
vy0 = v * np.sin(alpha)
m = 0.5
F = 0.1 * m * v**2


z0 = x0, vx0, y0, vy0

sol = odeint(move_func, z0, t)


def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
  
# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r')
ball_line, = plt.plot([], [], '-', color='r')


def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))


ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 100
ax.set_xlim(-edge, edge)
	
ax.set_ylim(0, edge)
 
ani.save('animation.gif')