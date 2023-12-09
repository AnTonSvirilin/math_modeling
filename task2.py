## Создать функцию, строящую график гиперболы, заданной явно.
## На вход, функции подаются пределы изменения переменной x и количество точек N, на которое разбиваются соответствующие пределы.

import matplotlib.pyplot as plt
import numpy as np
 
def hyperbola_plotter(a = 3, b = 5, N = 50):
 
    x = np.linspace(-a, a, N)
    y = 3/x
    
 
    plt.plot(x, y, label='my hyperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('hyperbola')
    plt.legend()
    
    plt.savefig('fig_574.png')
 
if __name__ == '__main__':
    hyperbola_plotter()