from const import g

def meh_energy(m, h, V, g):
    p = m*g*h
    k = (m*(V**2))/2
    E = p + k
    return p, k, E

m = int(input())
h = int(input())
V = int(input())

print(meh_energy(m, h, V, g))