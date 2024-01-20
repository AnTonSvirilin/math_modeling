import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Создание прямоугольника для картошки фри
potato_rect = plt.Rectangle((0, 10), 2, 1, fc='yellow')
ax.add_patch(potato_rect)

# Создание прямоугольника для лужи
puddle_rect = plt.Rectangle((0, 0), 10, 2, fc='blue')
ax.add_patch(puddle_rect)

def update(frame):
    if frame < 10:
        # Падение картошки фри
        potato_rect.set_xy((0, 10 - frame))
    else:
        # "Растекание" картошки фри в лужу
        potato_rect.set_visible(False)
        puddle_rect.set_visible(True)
        puddle_rect.set_height(puddle_rect.get_height() + 0.1)
        puddle_rect.set_y(0)
    
    return potato_rect, puddle_rect

def init():
    return potato_rect, puddle_rect

ani = animation.FuncAnimation(fig, update, frames=20, init_func=init, blit=True)

plt.show()