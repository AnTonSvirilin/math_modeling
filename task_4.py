################ Задача №4 (практикум №2, основной блок)

n = int(input())
a1 = 0
a2 = 1

for i in range(n+1):
    a2 = a1 + a2
    a1 = a2 - a1
    print(a1)