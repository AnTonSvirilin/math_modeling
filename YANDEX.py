import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x, y):
    return [
        y[1] + x[0] * (y[0] - y[2]),
        x[1] + y[0] * y[2],
        -y[0] + x[2]
    ]

def point_on_curve(t):
    y = odeint(f, [0, 0, 0], t)
    return y[0][0], y[0][1]

t = np.linspace(0, 50, 5001)
y0 = [0, 0, 0]
y = odeint(f, y0, t)
point_x, point_y = point_on_curve(t)

fig, ax = plt.subplots()
ax.plot(y[:, 0], y[:, 1], color='black', linestyle=' ', marker='.', markersize=2)
ax.scatter(point_x, point_y, color='red', marker='o', s=10)

def animate(i):
    point_x, point_y = point_on_curve(i)
    ax.scatter(point_x, point_y, color='red', marker='o', s=10)
    fig.canvas.draw_idle()

ani = FuncAnimation(fig, animate, frames=t, interval=100)
ani.save('animation.gif')