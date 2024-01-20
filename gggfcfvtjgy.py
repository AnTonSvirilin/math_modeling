import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

plt.xlabel('Coord: x') 
plt.ylabel('Coord: y') 
plt.title('физика - лженаука') # Общая подпись графика

# Создание картошки фри
potato_rect = plt.Rectangle((0.4, 0.9), 0.2, 0.05, color='orange', label = 'fries')
ax.add_patch(potato_rect)
# Создание лужи 
puddle = plt.Rectangle((0.3, 0), 0.4, 0.2, color='blue', label = 'puddle')
ax.add_patch(puddle)

plt.legend() 
def update(frame):
    if frame < 45:
        # Падение картошки фри в лужу
        potato_rect.set_y(potato_rect.get_y() - 0.02)
    else:
            # Растекание лужи вправо и влево
        if frame % 2 == 0:
            #Смещение лужи вправо
            puddle.set_width(puddle.get_width() + 0.02)       

            puddle.set_x(puddle.get_x() - 0.02)
            # Смещение лужи влево
            puddle.set_width(puddle.get_width() + 0.02)

    return potato_rect, puddle
#Функция init используется для инициализации начального состояния анимации.
def init():
    return potato_rect, puddle

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# 1 единица на оси x будет равна 1 единице на оси y визуально
plt.axis('scaled')
plt.xlim(0, 1)
plt.ylim(0, 1)
ani.save('killme.gif')