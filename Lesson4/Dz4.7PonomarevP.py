from math import factorial


def fact(x):
    y = 1
    z = 1
    while x > 0:
        y = 1
        for i in range(1, z + 1):
            y = y * i
        z += 1
        x -= 1
        yield y


n = int(input('Enter number: '))

for stat, e1 in enumerate(fact(n)):
    print(f'{stat + 1}! = {e1}')

print('\nAnother way: \n')

for e2 in range(1, n + 1):
    print(f'{e2}! = {factorial(e2)}')
