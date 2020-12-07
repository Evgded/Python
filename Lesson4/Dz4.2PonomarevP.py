my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [x for i, x in enumerate(my_list[1:]) if x > my_list[i]]
print(new_list)
