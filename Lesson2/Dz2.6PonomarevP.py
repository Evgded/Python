i = None
list_of_goods = []
number = 1
cost = 0
quantity = 0
while i != 'нет':
    name = input('Ведите название товара: ')
    try:
        cost = int(input('Ведите цену товара: '))
    except ValueError:
        print('Буквы нельзя!')
        continue
    try:
        quantity = int(input('Введите количество: '))
    except ValueError:
        print('Буквы нельзя!')
        continue
    unit = input('Введите единицы измерения: ')
    features = {'Название': name, 'Цена': cost, 'Количество': quantity, 'Ед.изм.': unit}
    one_good = (number, features)
    list_of_goods.append(one_good)
    number += 1
    i = input('Хотите ввести еще один товар (да/нет): ')
for e1 in list_of_goods:
    print(e1)
position = 0
all_names = []
all_costs = []
all_quantities = []
all_units = []
while position < len(list_of_goods):
    all_names.append(list_of_goods[position][1].get('Название'))
    all_costs.append(list_of_goods[position][1].get('Цена'))
    all_quantities.append(list_of_goods[position][1].get('Количество'))
    all_units.append(list_of_goods[position][1].get('Ед.изм.'))
    position += 1
print('Названия: ', all_names)
print('Цены: ', all_costs)
print('Количество: ', all_quantities)
print('Ед.изм.: ', all_units)
