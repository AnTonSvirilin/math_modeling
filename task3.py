import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
t = np.arange(-5, 5, 0.1)


def diff_func(s, t): 
    y, w = s
	
    dy_dt = w
    dw_dt = np.sin(t) + np.cos(t)
    
    return dw_dt, dy_dt

w0 = 0
y0 = 3

s0 = y0, w0

sol = odeint(diff_func, s0, t)

	
plt.plot(t, sol[:, 0], 'b')
 
plt.legend()
plt.savefig('fig_3.png')