from math import pi

t = str(input("фигура"))
a, b, h, R = int(input()), int(input()), int(input()), int(input())

def square(t, a, b, h, R):
    if t == 'круг':
        s = pi * R**2
        return s
    elif t == 'прямоугольник':
        s = a*b
        return s
    elif t == 'треугольник':
        s = (a*h)/2
        return sorted
    else:
        print('вы ввели недопустимую фигуру')
        return 0
    
print(square(t, a, b, h, R))
