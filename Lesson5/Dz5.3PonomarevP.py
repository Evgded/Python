salaries = []
with open('Text5.3.txt') as f_obj:
    txt_lines = f_obj.readlines()
    for i in txt_lines:
        txt = i.split()
        person = {txt[0] + ' ' + txt[1] + ' ' + txt[2]: int(txt[3])}
        if int(txt[3]) < 20000:
            print(txt[0] + ' ' + txt[1] + ' ' + txt[2], 'salary is less than 20k!', '(', txt[3], ')')
        salaries.append(int(txt[3]))
print('Our average salary is: ', sum(salaries) / len(salaries))
