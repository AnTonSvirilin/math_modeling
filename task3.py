import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,360,360)

x =10*np.cos(np.radians(t)) 
y = 50*np.sin(np.radians(t))

plt.plot(x,y)

plt.savefig('figplshelp.png')