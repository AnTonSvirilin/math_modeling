##############Задача №2 (практикум №3, основной блок)

import math 
from task_1_constants import g, e, h, k

h = 100
a = math.pi/3
b = 30

V = math.sqrt((g*h * math.tan(b)**2)/(2 * math.cos(a)**2 * (1 - math.tan(b)*math.tan(a))))

print(V)

T = 200
E = 300

N = (2/math.sqrt(math.pi)) * (h/(k*T)**(3/2)) * (e ** (-E/k*T)) * (E ** (T/2))

print(N)
