sentence = input('Введите предложение: ')
print(sentence)
my_list = sentence.split()
print(my_list)
for ind, i in enumerate(my_list, 1):
    print(ind, i[:10].title())
