my_exams = {}
with open('Text5.6.txt') as f_obj:
    txt_lines = f_obj.readlines()
    for e1 in txt_lines:
        txt = e1.split()
        name = list(txt[0])
        name.remove(':')
        real_name = ''.join(name)
        number_exams = []
        for e2 in txt:
            number = e2.split('(')
            try:
                number_exams.append(int(number[0]))
            except ValueError:
                continue
        my_exams.update({real_name: sum(number_exams)})
print(my_exams)
