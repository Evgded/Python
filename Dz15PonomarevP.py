revenue = float(input('Сколько в этом периоде выручили: '))
costs = float(input('Сколько в этом месяце потратили: '))
profitability = 0
profit = revenue - costs

if revenue < costs:
    print('Казна пустеет, Милорд!')
elif revenue == costs:
    print('Нужно боольше золота!')
else:
    print('Работем в плюс, красавчик!')
    profitability = profit / revenue
    manNumber = int(input('Сколько нас трудилось: '))
    usefulness = profit / manNumber
    print('Каждый нам сдлал: ', usefulness)
