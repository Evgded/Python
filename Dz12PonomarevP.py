time = int(input('Введите время в секундах: '))
print('Вы ввели: ', time)
print(type(time))
hour = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f'Time now is: {hour:02d}:{minutes:02d}:{seconds:02d}')
