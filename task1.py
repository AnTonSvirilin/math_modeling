import random

N = int(input())

a = [random.randint(0, 100) for i in range(N)]
b = [random.randint(0, 100) for i in range(N)]
c = [random.randint(0, 100) for i in range(N)]

max1 = max(a)
max2 = max(b)
max3 = max(c)

maxx = max(max1, max2, max3)
print(maxx)

summ = sum(a) + sum(b) + sum(c)

print(summ)