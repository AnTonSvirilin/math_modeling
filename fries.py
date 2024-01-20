import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Инициализация позиции картошки и лужи
potato_position = np.array([0, 10])
puddle_position = np.array([5, 0])

# Отрисовка картошки и лужи
potato, = ax.plot([], [], 'bo', markersize=10)
puddle, = ax.plot(puddle_position[0], puddle_position[1], 'b')

# Функция для инициализации анимации
def init():
    potato.set_data([], [])
    return potato,

# Функция для обновления позиции картошки
def update(frame):
    potato_position[1] -= 0.5  # Симуляция падения
    potato.set_data(potato_position[0], potato_position[1])

    return potato,

# Создание анимации
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 20), init_func=init, interval=100, blit=True)

plt.xlim(0, 10)
plt.ylim(0, 15)
plt.show()
ani.save('falling_potato.gif')