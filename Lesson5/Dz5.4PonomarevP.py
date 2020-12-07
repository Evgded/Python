from translate import Translator

ts = Translator(to_lang='ru')

with open('Text5.4.1.txt') as f_obj:
    txt_lines = f_obj.readlines()
    for e1 in txt_lines:
        txt = e1.split()
        txt[0] = ts.translate(txt[0])
        s_obj = open('Text5.4.2.txt', 'a')
        for e2 in txt:
            s_obj.write(e2 + ' ')
        s_obj.write('\n')
        s_obj.close()
