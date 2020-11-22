months = {'first_season': 'Лето', 'second_season': 'Осень', 'third_season': 'Зима', 'fourth_season': 'Весна'}
number = 0
while True:
    try:
        number = int(input('Введите номер месяца: '))
        break
    except ValueError:
        print('Ай, не балуйся!')
        continue
if number == 1 or number == 2 or number == 12:
    print('Сейчас: ', months.get('third_season'))
elif number == 3 or number == 4 or number == 5:
    print('Сейчас: ', months.get('fourth_season'))
elif number == 6 or number == 7 or number == 8:
    print('Сейчас: ', months.get('first_season'))
elif number == 9 or number == 10 or number == 11:
    print('Сейчас: ', months.get('second_season'))
else:
    print('Ну и не узнаешь, что сейчас.. (')
