f_obj = open('Text5.5.txt', 'w+')
f_obj.write('1 2 3 4 5 6 7 8 9 23 34 3456 12354 5435 2')
f_obj.seek(0)
my_int = f_obj.readline().split()
my_sum = 0
for i in my_int:
    my_sum += int(i)
print('Sum is:', my_sum)
f_obj.close()
