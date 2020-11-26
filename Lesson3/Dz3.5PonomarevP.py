def my_sum(numbers):
    return sum(numbers)


quit_stat = None
sum_list = []
i = 0
while True:
    in_numbers = input('Введите числа через пробел (Для остановки введите Q): ').split()
    for i in in_numbers:
        if i.lower() == 'q':
            quit_stat = 0
            break
        else:
            sum_list.append(int(i))
    print('Сумма введенных чисел: ', my_sum(sum_list))
    if quit_stat == 0:
        break
print('Сумма всех введенных чисел: ', my_sum(sum_list))
