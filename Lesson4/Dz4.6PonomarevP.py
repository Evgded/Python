from itertools import count, cycle

start = int(input('Enter start number: '))
for i in count(start):
    if i > 10:
        break
    else:
        print(i)
my_list = list(input('Enter list of objects: ').split())
print(my_list)
stop = 0
for i in cycle(my_list):
    if stop > 10:
        break
    else:
        print(i)
    stop += 1
