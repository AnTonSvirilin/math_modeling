###Задача №4 (практикум №4, основной блок)###
k = []
def ourfunc(a, b, x):
    c = (a-b)/(n-1)
    
    for i in range(n):
        x = a + i*c
        y = x**2
        k.append(y)
    return k


a, b = int(input('число а меньше б')), int(input())
x = int(input('a<x<b'))
n = int(input())

print(ourfunc(a, b, x))