def my_sum(x, y, z):
    try:
        my_list = [int(x), int(y), int(z)]
        my_list.remove(min(my_list))
        print('Максимальные из них: ', my_list)
        return sum(my_list)
    except ValueError:
        print('Буквы нельзя')


numbers = input('Введите три числа через пробел: ').split()
print('Сумма больших из них: ', my_sum(numbers[0], numbers[1], numbers[2]))
