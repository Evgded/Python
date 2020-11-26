def my_degree(x, y):
    z = 1
    try:
        x = int(x)
        y = int(y)
        while abs(y) > 0:
            z = z * (1 / x)
            y += 1
        return z
    except ValueError:
        print('Буквы нельзя')


numbers = input('Введите два числа через пробел положительное и отрицательное: ').split()
print('Результат их деления: ', my_degree(numbers[0], numbers[1]))
