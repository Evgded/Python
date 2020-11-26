def my_degree(x, y):
    try:
        x = float(x) ** int(y)
        return x
    except ValueError:
        print('Буквы нельзя')


numbers = input('Введите два числа через пробел положительное и отрицательное: ').split()
print('Результат их деления: ', my_degree(numbers[0], numbers[1]))
