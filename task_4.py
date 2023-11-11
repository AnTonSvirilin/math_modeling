import numpy as np
from math import sin

N = int(input("Введите значение N: "))
M = int(input("Введите значение M: "))
zero_index = input("Используется ли индексация с нуля? ")

if zero_index == 'да':
    array = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            a = sin(N*(i+1) + M*(j+1))
            if a < 0:
                array[i, j] = 0
            else:
                array[i, j] = a
else:
    array = np.zeros((N+1, M+1))
    for i in range(1, N+1):
        for j in range(1, M+1):
            a = sin(N*i + M*j)
            if a < 0:
                array[i, j] = 0
            else:
                array[i, j] = a
    
 

print(array)
