with open('text_6.txt', 'r', encoding='utf-8') as file:
    my_dict = {}

    for line in file.readlines():
        key = line.split()[0].replace(':', '')
        line = line.replace('-', '0').replace('(пр)', '').replace('(л)', '').replace('(лаб)', '').split()[1:]
        sum_line = sum(map(int, line))
        my_dict[key] = sum_line

    print(my_dict)
