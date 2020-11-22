# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
# number_int = int(input('Введите целое число: '))
# my_list.append(number_int)
# number_float = float(input('Введите дробное число: '))
# my_list.append(number_float)
# my_str = input('Введите слово: ')
# my_list.append(my_str)
# my_bool = bool(input('Введите True/False: '))
# my_list.append(my_bool)
my_list = [1234, 56.78, 'Здесь буквы', True]
print(my_list)
print(f'Первый член списка: {my_list[0]}; его тип: {type(my_list[0])}')
print(f'Второй член списка: {my_list[1]}; его тип: {type(my_list[1])}')
print(f'Третий член списка: {my_list[2]}; его тип: {type(my_list[2])}')
print(f'Четвертый член списка: {my_list[3]}; его тип: {type(my_list[3])}')
