x0 = 10 # Переменная в глобальной области видимости

def move(t):
    x = x0 * t
    return x

print(move(3))   #30
print(x)         #NameError: name 'x' is not defined
a = 'Good'

def my_func():
    a = 'Bad'
    print(a)      #Bad

my_func()
print(a)          #Good