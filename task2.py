import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
t = np.arange(-1, 1, 0.1)


def diff_func(s, t): 
    y, x = s
	
    # Первое уравнение системы
    dx_dt = 3*x - 2*y + (e**(3*t))/(e**t + 1)
    # Второе уравнение системы
    dy_dt = x - (e**(3*t)/(e**t + 1))
    
    return dx_dt, dy_dt

x0 = 5
y0 = -7
e=np.e

s0 = y0, x0

sol = odeint(diff_func, s0, t)

	
plt.plot(t, sol[:, 0], 'b')
 
plt.legend()
plt.savefig('fig_2.png')