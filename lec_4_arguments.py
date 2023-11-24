def my_func(a, b):
    x = 3 * a - b
    return x

tmp = my_func()               #TypeError: my_func() missing  2 required positional arguments: 'a' and 'b'

def my_func(a=1, b=0):
    x = 3 * a - b
    return x

print(my_func())   #3
print(my_func(3, 4))  #5
print(my_func(3))   #9
print(my_func(b=3))  #0
print(my_func(b=3, a=9))    #24



def my_func(a, b=0):
    x = 3 * a - b
    return x

# Так НЕЛЬЗЯ!
# def my_func(a=0, b):
#     x = 3 * a - b
#     return x

def my_func(*args):              #аргументы
    x = 3 * args[0] - args[1]
    return x

print(my_func(3, 4))          #5
print(my_func(3, 4, 8))       #5



def my_func(**kwrgs):                        #словарь"
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x

print(my_func(obj_1=3, obj_2=4))               #5
print(my_func(obj_1=3, obj_2=4, obj_3=8))      #5



