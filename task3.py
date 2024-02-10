#На материальную точку массы m действует постоянная сила, сообщающая точке ускорение a0. Окружающая среда оказывает движущейся точке сопротивление,
# пропорциональное квадрату скорости движения со временем, коэффициент сопротивления равен γ. Определите закон изменения скорости со временем, 
#если в начальный момент времени точка находилась в покое.


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0, 4, 1)

n_0 = 100

def invest(n, t):
    dndt = - k * n_0
    return dndt

k = 0.8


m_t = odeint(invest, n_0, t)

plt.plot(t, m_t[:,0], label='nydtcnbwbb')

plt.savefig('fig3.png')