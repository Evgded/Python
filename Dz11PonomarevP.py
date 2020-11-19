print('Helo world, it\'s me!')
me_int = 256
small = 'Че так мало?'
norm = 'нромально'
beauty = 'ваще'
print(me_int)
print(norm)
print(beauty)
me_float = float(input('Введите любое число: '))

if me_float <= 100:
    print(small)
elif me_float <= 1000:
    print('Уже ' + norm)
else:
    print('Теперь ', beauty, ' молодца')
