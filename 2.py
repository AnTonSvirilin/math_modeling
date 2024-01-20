import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = 0
y = 10
v = 0
g = 9.81
t = 0
dt = 0.1

def update(frame):
    global x, y, v, t
    t += dt
    x = 0
    y = 10 - 0.5 * g * t**2
    v = g*t
    if y < 0:
        y = 0
        v = 0
    scatter.set_offsets(np.c_[x, y])
    return scatter,

scatter = ax.scatter(x, y, marker='o', color='brown')

ax.set_xlim(-10, 10)
ax.set_ylim(0, 10)

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 10, 0.1), blit=True)

plt.show()

ani.save('falling_potato_pt2.gif')