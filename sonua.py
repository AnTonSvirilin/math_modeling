import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Создаем новую фигуру
fig, ax = plt.subplots()

# Радиусы ядра и электронных слоев
core_radius = 0.1
electron_layer1_radius = 0.5
electron_layer2_radius = 0.9

# Создаем ядро
core = plt.Circle((0, 0), core_radius, color='red')
ax.add_patch(core)

# Создаем электронные слои
electron_layer1 = plt.Circle((0, 0), electron_layer1_radius, color='blue', fill=False, linestyle='dotted')
ax.add_patch(electron_layer1)
electron_layer2 = plt.Circle((0, 0), electron_layer2_radius, color='blue', fill=False, linestyle='dotted')
ax.add_patch(electron_layer2)

# Начальные положения протонов и нейтронов
num_particles = 20
particle_positions = np.random.rand(num_particles, 2) * 2 * core_radius - core_radius

# Создаем отображение для каждой частицы
particles, = ax.plot([], [], 'bo', ms=8)  # В этом примере мы будем использовать точки для представления частиц

# Функция инициализации анимации
def init():
    particles.set_data([], [])
    return particles,

# Функция обновления кадра анимации
def update(frame):
    if not hasattr(update, "particle_positions"):
        update.particle_positions = np.random.rand(num_particles, 2) * 2 * core_radius - core_radius
    # Двигаем частицы случайным образом
    update.particle_positions += np.random.randn(num_particles, 2) * 0.01
    particles.set_data(update.particle_positions[:,0], update.particle_positions[:,1])

    return particles,

    return particles,

# Создаем анимацию
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True)

# Сохраняем анимацию в виде файла
ani.save('oxygen_atom_animation.gif', writer='imagemagick', fps=30)
