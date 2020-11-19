number = int(input('Введите любое число: '))

if number < 0:
    number = number * -1

check = 0

while number >= 1:
    digit = number % 10
    number = number // 10
    if check < digit:
        check = digit
    if check == 9:
        break

print('Самая большая цифра в вашем числе: ', check)
