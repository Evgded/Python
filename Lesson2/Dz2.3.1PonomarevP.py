months = ['Лето', 'Осень', 'Зима', 'Весна']
number = 0
while True:
    try:
        number = int(input('Введите номер месяца: '))
        break
    except ValueError:
        print('Ай, не балуйся!')
        continue
if number == 1 or number == 2 or number == 12:
    print('Сейчас: ', months[2])
elif number == 3 or number == 4 or number == 5:
    print('Сейчас: ', months[3])
elif number == 6 or number == 7 or number == 8:
    print('Сейчас: ', months[0])
elif number == 9 or number == 10 or number == 11:
    print('Сейчас: ', months[1])
else:
    print('Ну и не узнаешь что сейчас.. (')
