##############Задача №2 (практикум №2, дополнительный блок)
a, b, c = int(input()), int(input()), int(input())

if a < b+c and b < a+c and c < a+b:
    if a == b == c:
        print('треугольник равносторонний')
    elif a == b or a ==c or b == c:
        print('треуголльник равнобедренный')
    else:
        print('треугольник разносторнний')
else:
    print('такого треуголька не существует')