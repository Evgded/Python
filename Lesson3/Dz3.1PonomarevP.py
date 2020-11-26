def my_div(x, y):
    try:
        x = int(x) / int(y)
        return x
    except ValueError:
        print('Буквы нельзя')
    except ZeroDivisionError:
        print('Деление на ноль')


numbers = input('Введите два числа через пробел: ').split()
print('Результат их деления: ', my_div(numbers[0], numbers[1]))
