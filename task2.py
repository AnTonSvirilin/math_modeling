import numpy as np

a = np.array([1, 2, 3, 4, 5])

def multiply(a):
    res = np.prod(a)
    return res

print(multiply(a))