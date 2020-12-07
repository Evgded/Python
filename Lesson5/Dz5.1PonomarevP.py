txt = None
with open('Text5.1.txt', 'r+') as f_obj:
    while True:
        txt = input('Enter string to write in file (to stop enter empty string): ')
        if not txt:
            break
        f_obj.write(txt + "\n")
    f_obj.seek(0)
    out_txt = f_obj.read()
print(out_txt)
