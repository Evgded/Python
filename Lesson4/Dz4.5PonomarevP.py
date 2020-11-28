from functools import reduce

my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(my_list)
print(reduce(lambda p_1, p_2: p_1 * p_2, my_list))
print(len(str(reduce(lambda p_1, p_2: p_1 * p_2, my_list))))
