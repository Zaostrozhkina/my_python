import json

with open('text_7.txt', 'r', encoding='utf-8') as my_file:
    dict_profit = {}
    dict_avarage_profit = {}
    list_profit = []
    for line in my_file.readlines():
        profit = int(line.split()[2]) - int(line.split()[3])
        dict_profit[line.split()[0]] = profit
        if profit > 0:
            list_profit.append(profit)

    # print(dict_profit)

    average_profit = sum(list_profit) / len(list_profit)
    dict_avarage_profit['average_profit'] = average_profit
    # print(dict_avarage_profit)

    my_list = [dict_profit, dict_avarage_profit]
    #print(my_list)

    with open('5_7.json', 'w', encoding='utf-8') as json_file:
        json.dump(my_list, json_file, ensure_ascii=False, indent=4)
