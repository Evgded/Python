i = 1
firstDay = 0
allWay = 0

while i == 1:
    firstDay = float(input('Введите количество километров в первый день: '))
    allWay = float(input('Сколько надо пробегать: '))
    if allWay < firstDay or firstDay < 0 or allWay < 0:
        print('Ну и дурак =)')
        continue
    else:
        break

progress = 1

while firstDay < allWay:
    progress += 1
    firstDay *= 1.1
    print(firstDay)

print('Превозмогем за: ', progress, 'дней!11!')
