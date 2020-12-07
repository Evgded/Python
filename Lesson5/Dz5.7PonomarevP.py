import json

my_firms = {}
one_firm = {}
all_profits = []
with open('Text5.7.1.txt') as f_obj:
    txt_lines = f_obj.readlines()
    for i in txt_lines:
        txt = i.split()
        profit = int(txt[2]) - int(txt[3])
        if profit > 0:
            all_profits.append(profit)
        my_firms.update({txt[0]: profit})
average_profit = sum(all_profits)/len(all_profits)
print('Our average profit is: ', average_profit)
all_info = [my_firms, {'Average_profit': average_profit}]
print(all_info)
with open('Text5.7.2.txt', 'w') as j_obj:
    json.dump(all_info, j_obj)
