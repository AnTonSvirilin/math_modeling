import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Создание картошки фри (оранжевый прямоугольник)
potato_rect = plt.Rectangle((0.4, 0.9), 0.2, 0.05, fc='orange')
ax.add_patch(potato_rect)

# Создание лужи (голубой овал)
puddle_oval = plt.Rectangle((0.3, 0.4), 0.4, 0.2, fc='blue')
ax.add_patch(puddle_oval)

def update(frame):
    if frame < 50:
        # Падение картошки фри в лужу
        potato_rect.set_y(potato_rect.get_y() - 0.02)
    else:
        # Растекание лужи вправо и влево
        if frame % 2 == 0:
            puddle_oval.set_width(puddle_oval.get_width() + 0.02)
            puddle_oval.set_x(puddle_oval.get_x() - 0.01)
        else:
            puddle_oval.set_width(puddle_oval.get_width() + 0.02)
    
    return potato_rect, puddle_oval

def init():
    return potato_rect, puddle_oval

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

plt.axis('scaled')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()