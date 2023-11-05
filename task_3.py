##########Задача №3 (практикум №3, основной блок)
from task_1_constants import g
x0 = 3
V0x = 6
y0 = 6
V0y = 2
x = 0
y = 0
result = []
T = [0, 1, 2, 3, 4, 5]
for t in range(0, 6, 1):
    x = x0 + V0x*t
    y = y0 + V0y*y - (g* t**2)/2
    result.append([t, x, y])


for i in result:
    print(i)