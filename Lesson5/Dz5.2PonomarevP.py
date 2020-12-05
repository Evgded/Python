with open('Text5.2.txt') as f_obj:
    txt_lines = f_obj.readlines()
print('Number of strings: ', len(txt_lines))
for num, i in enumerate(txt_lines):
    print(f'Number of words in {num + 1} string is: {len(i.split())}')
