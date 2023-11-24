def changer(a, b):
    a = 2
    b[0] = 'Good'

x = 10
L = [1, 2]

changer(x, L)

print(x)   #10
print(L)   #['Good', 2]

L = [1, 2]
changer(x, L[:])

print(L)     #[1, 2]





# Coplex numbers
x = 3
y = 4

z = complex(x,y)
print(z)              #(3+4j)

w = complex(y, x)

print(z + w)          #(7+7j)


# Strings
s = 'hello'
print(s[0])           #h

s[0] = 'H'            #TypeError: 'str' object does not support item assignment



# Tuple
t = (1, 4, 9)
print(t)         #(1, 4, 9)
print(t[0])      #1
t[0] = 3         ##TypeError: 'tuple' object does not support item assignment

# list
l = [1, 4, 9]
l[0] = 3
print(l)        #[3, 4, 9]

# Dict
d = {'a1':4, 4:'a1', 'str':'Hello'}
print(d['a1'])                       #4
print(d[4])                          #a1
print(d['str'])                      #Hello

d['str'] = 'Good'
print(d)                            #{'a1': 4, 4: 'a1', 'str': 'Good'}
