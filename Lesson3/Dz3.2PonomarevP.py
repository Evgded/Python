def my_func(**kwargs):
    print(f'Данные о персоне: {kwargs}')


person = input('Введите Имя, Фамилию, Год рождения, Город проживания, e-mail и Телефон через пробел: ').split()
my_func(name=person[0], Фамилия=person[1], Год_рождения=person[2], Город=person[3], e_mail=person[4], Телефон=person[5])
