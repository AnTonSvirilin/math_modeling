#Из эксперимента известно, что скорость размножения бактерий при достаточном запасе пищи пропорциональна их количеству. 
#Определите закон увеличения бактерий и время, спустя которое их станет в 10 раз больше, относительно начального количества.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 50, 0.1)

n_0 = 5

def bacteria(n, t):
    dndt = k * n
    return dndt

k = 0.1


m_t = odeint(bacteria, n_0, t)

plt.plot(t, m_t[:,0], label='распад бактерий')

plt.savefig('fig22.png')
