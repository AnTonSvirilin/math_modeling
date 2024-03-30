import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
a,b,c=0.398,2.0,4.0
def f(y, t):
    y1, y2, y3 = y
    return [(-y2-y3),
    y1+a*y2,
    b+y3*(y1-c)]
t = np.linspace(0,50,5001)
y0 = [0,0, 0]
[y1,y2,y3]=odeint(f, y0, t, full_output=False).T
plt.plot(y1,y2, color='black', linestyle=' ', marker='.',
markersize=2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title("Проекция ленты Ройсслера на плоскость xy")
plt.savefig("1")