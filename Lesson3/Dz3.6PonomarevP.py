def int_func(string):
    return string.title()


print(int_func('text'))
my_sentence = input('Введите предлоджение с маленьких букв: ')
print('А надо было так: ', int_func(my_sentence))
