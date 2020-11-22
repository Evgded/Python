my_list = []
i = None
while i != 'нет':
    member = input('Ведите элемент списка: ')
    my_list.append(member)
    i = input('Хотите ввести еще один элемент (да/нет): ')
print(my_list)
e1 = 0
while True:
    try:
        my_list[e1], my_list[e1 + 1] = my_list[e1 + 1], my_list[e1]
    except IndexError:
        break
    e1 += 2
print(my_list)
