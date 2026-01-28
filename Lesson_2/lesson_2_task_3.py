import math


def square(side):
    area = side ** 2
    if isinstance(side, int) or (isinstance(side, float)
                                 and side.is_integer()):
        return int(area)
    else:
        return math.ceil(area)


num_side = float(input("Введите размер стороны квадрата: "))
result = square(num_side)
print(f"площадь квадрата: {result}")
