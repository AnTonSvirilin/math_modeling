import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Создание картошки фри (желтый прямоугольник)
potato_rect = plt.Rectangle((0.5, 0.9), 0.2, 0.1, fc='yellow')
ax.add_patch(potato_rect)

# Создание лужи (голубой овал)
puddle_oval = plt.Rectangle((0.4, -0.4), 0.4, 0.2, fc='blue')
ax.add_patch(puddle_oval)

def update(frame):
    if frame < 50:  # 50 кадров, чтобы анимация длилась 5 секунд
        # Падение картошки фри в лужу
        potato_rect.set_y(potato_rect.get_y() - 0.02)
    else:
        # Растекание лужи
        puddle_oval.set_height(puddle_oval.get_height() - 0.02)
        puddle_oval.set_y(puddle_oval.get_y() - 0.01)
    
    return potato_rect, puddle_oval

def init():
    return potato_rect, puddle_oval

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

plt.show()