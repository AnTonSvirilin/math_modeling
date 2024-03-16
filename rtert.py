import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры модели маятника
g = 9.81  # ускорение свободного падения
L = 1.0  # длина маятника

# Определение функции дифференциального уравнения для моделирования движения маятника
def pendulum_ode(y, t):
    theta, omega = y
    dydt = [omega, -g/L * np.sin(theta)]
    return dydt

# Начальные условия
y0 = [np.pi/4, 0.0]  # начальный угол и начальная угловая скорость
t = np.linspace(0, 10, 1000)  # Временные точки для решения дифференциального уравнения

# Решение дифференциального уравнения
sol = odeint(pendulum_ode, y0, t)

# Построение графика угла маятника от времени
plt.plot(t, sol[:, 0], 'b', label='Угол маятника')
plt.xlabel('Время (сек)')
plt.ylabel('Угол (рад)')
plt.title('Модель маятника')
plt.grid()
plt.legend()
plt.save('vhwh.gif')