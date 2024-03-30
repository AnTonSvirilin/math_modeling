import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a, b, c = 0.398, 2.0, 4.0

def f(y, t):
    y1, y2, y3 = y
    return [(-y2 - y3), y1 + a*y2, b + y3*(y1 - c)]

t = np.linspace(0, 50, 5001)
y0 = [0, 0, 0]
y = odeint(f, y0, t)

fig, ax = plt.subplots()
line, = ax.plot(y[:,0], y[:,1], color='black', linestyle='-', marker='')
point, = ax.plot(y[0,0], y[0,1], color='red', marker='o')

def update(frame):
    point.set_data([y[frame,0]], [y[frame,1]])
    line.set_data(y[:frame, 0], y[:frame, 1])  # обновляем траекторию

ani = animation.FuncAnimation(fig, update, frames=len(t), blit=False)

ani.save('2.gif', writer='pillow')