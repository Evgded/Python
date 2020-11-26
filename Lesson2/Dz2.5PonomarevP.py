my_list = [9, 9, 5, 3, 3, 1]
number = int(input('Введиет позицию в рейтинге: '))
i = 0
for e1 in my_list:
    if e1 <= number:
        my_list.insert(i, number)
        break
    i += 1
print(my_list)
