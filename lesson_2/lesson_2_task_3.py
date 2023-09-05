import math
def square(c):
    s=(c*c)

    print('Сторона квадрата: ', c)
    print('Площадь квадрата: ', math.ceil(s))

c=float(input('Введите сторону квадрата:'))
square(c)    